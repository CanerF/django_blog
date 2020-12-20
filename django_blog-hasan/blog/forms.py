from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['content'].widget.attrs['rows'] = 10

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 250:
            content = len(content)
            msg = 'Lütfen en az 250 karakter giriniz. Girilen karakter sayısı (%s)' % (uzunluk)
            raise forms.ValidationError(msg)
        return content
