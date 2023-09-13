from django.shortcuts import render


# Create your views here.
def home(request):
    template_name = 'home.html'

    return render(request, template_name)


def words_list(request):
    template_name = 'words_list.html'

    return render(request, template_name)


def add_word(request):
    template_name = 'add_word.html'

    return render(request, template_name)