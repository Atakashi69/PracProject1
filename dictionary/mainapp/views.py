from django.shortcuts import render
from .mainapp_utils import filerw


# Create your views here.
def home(request):
    template_name = 'home.html'

    return render(request, template_name)


def words_list(request):
    template_name = 'words_list.html'

    words_ru, words_en = filerw.get_words()
    words = zip(words_ru, words_en)

    context = {
        'words': words
    }

    return render(request, template_name, context=context)


def add_word(request):
    template_name = 'add_word.html'

    return render(request, template_name)