from django import forms

class AddWordForm(forms.Form):
    word_ru = forms.CharField(label="Слово на русском", max_length=100)
    word_en = forms.CharField(label="Перевод на английский", max_length=100)
