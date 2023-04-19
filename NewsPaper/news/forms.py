from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "img",
            "text",
            "category",
        ]

        widgets = {
            "author": forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'userid'}),
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "img": forms.FileInput(attrs={'class': 'form-control'}),
            "text": forms.Textarea(attrs={'class': 'form-control'}),
            "category": forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if len(title) < 24 or len(text) < 512:
            raise ValidationError(
                "Заголовок должен содержать минимум 24 символа, текст минимум 512 символа"
            )
        elif title[0].islower() or text[0].islower():
            raise ValidationError(
                "Заголовок и текст должны начинаться с заглавной буквы"
            )
        return cleaned_data

