from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.templatetags.static import static
from django.contrib.sessions.models import Session
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views import View
from django import forms
import json
import requests
import openai
from .models import Story
import os


chapter_str = ''
EXPECTATION_WORDS = '700'

openai.api_key=settings.OPENAI_SECRET_KEY
api_url = 'https://api.openai.com/v1/chat/completions'


@method_decorator(csrf_protect, name='dispatch')
class GenerateStoryView(TemplateView):
    model = Story
    template_name = 'generate.html'

    def post(self, request, *args, **kwargs):
        user_question = request.POST.get('text-field')
        age = request.POST.get('age-field')
        chapter = request.POST.get('chapter-field')
        language = request.POST.get('language-field')

        # Retrieve chapter_str from the session
        chapter_str = request.session.get('chapter_str', '')

        if 'search_btn' in request.POST:
            user_result = (
                "Create a dictionary. where key=1, value=string. string values are chapter. These are " + chapter +
                " chapters heading for " + user_question + "."
            )

            payload_1 = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": user_result}],
                "temperature": 0.6,
                "top_p": 1.0,
                "stream": False,
                "presence_penalty": 0,
                "frequency_penalty": 0,
            }

            headers_1 = {
                "Content_Type": "application/json",
                "Authorization": f"Bearer {openai.api_key}"
            }

            response_1 = requests.post(url=api_url, headers=headers_1, json=payload_1, stream=False)

            if response_1.status_code == 200:
                try:
                    data = json.loads(response_1.content)
                    result_of_title = data['choices'][0]['message']['content']
                    print(result_of_title)

                except json.decoder.JSONDecodeError:
                    print("Error: Invalid JSON response")
                    print("Response Content:", response_1.text)

                try:
                    dictionary = eval(result_of_title)
                    if isinstance(dictionary, dict):
                        chapter_explanations = []
                        print(chapter_explanations)
                        for i in range(1, len(dictionary) + 1):
                            per_chapter = dictionary[i]
                            print(per_chapter)

                            chapter_explanations.append(f"Chapter-{i}-{per_chapter} \n")

                            language_field_2 = f"Write it in {language} language"
                            result = per_chapter + f" Explain it in {EXPECTATION_WORDS} words. {language_field_2}"
                            print(result)

                            payload_2 = {
                                "model": "gpt-4",
                                "messages": [{"role": "user", "content": result}],
                                "temperature": 0.1,
                                "top_p": 1.0,
                                "stream": False,
                                "presence_penalty": 0,
                                "frequency_penalty": 0,
                            }

                            headers_2 = {
                                "Content_Type": "application/json",
                                "Authorization": f"Bearer {openai.api_key}"
                            }

                            response_2 = requests.post(url=api_url, headers=headers_2, json=payload_2, stream=False)

                            data_2 = json.loads(response_2.content)

                            gpt_result = data_2['choices'][0]['message']['content']
                            print(gpt_result)

                            chapter_explanations.append(f"{gpt_result}\n\n\n")

                        # Update the session variable
                        chapter_str = "\n".join(chapter_explanations)
                        request.session['chapter_str'] = chapter_str

                        return render(request, self.template_name,
                                      context={'result': chapter_str, 'user_question': user_question, 'age': age,
                                               'language': language})
                    else:
                        print("The string does not represent a valid dictionary.")
                        print("Search Again.")
                except Exception as e:
                    print("An error occurred while converting the string to a dictionary:", e)
                    print("Restart Your Program.")


        elif 'save_btn' in request.POST:
            if chapter_str:
                input_story_name = request.POST.get('input-story-name')
                age = request.POST.get('user-age')
                language = request.POST.get('select-language')

                folder_name = 'Collection'
                if not os.path.exists(os.path.join(settings.STATIC_ROOT, folder_name)):
                    os.makedirs(os.path.join(settings.STATIC_ROOT, folder_name))

                file_path = os.path.join(settings.STATIC_ROOT, folder_name, f'{input_story_name}_story-0{age}12.txt')
                with open(file_path, 'w') as file:
                    file.write(chapter_str)

                story = Story(story_name=input_story_name, file=f'{input_story_name}_story', content=chapter_str, age=age, language=language)
                story.save()

                # Clear the session variable after saving
                request.session['chapter_str'] = ''

                return render(request, 'success.html', context={'story': story})
            else:
                print("Chapter_str is empty. Cannot save.")
                print("Check the 'search_btn' block.")
                return HttpResponse('Content not available')

        return render(request, self.template_name,
                      context={'result': chapter_str, 'user_question': user_question, 'age': age, 'language': language})
    


class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
    

class StoryListView(ListView):
    model = Story
    template_name = 'view_list.html'
    context_object_name = 'stories'

    def get_queryset(self):
        return super().get_queryset()


class StoryCURDForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['story_name']


class ViewTestFileView(View):
    template_name_with_mp3 = 'read_content_file.html'
    template_name_without_mp3 = 'voiceTest_and_download.html'

    def get(self, request, story_id, *args, **kwargs):
        story = get_object_or_404(Story, pk=story_id)
        file_path = os.path.join("Mp3", f"{story.story_name}_{story.id}.mp3")

        if os.path.exists(file_path):
            template_name = self.template_name_with_mp3
        else:
            template_name = self.template_name_without_mp3

        return render(request, template_name, {'story': story})
        
class StoryUpdateView(UpdateView):
    model = Story
    template_name = 'update_file.html'
    form_class = StoryCURDForm
    success_url = reverse_lazy('view_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = self.get_object()
        context['form'].initial['story_name'] = story.story_name
        return context