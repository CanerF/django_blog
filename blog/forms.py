from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
  
  

class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'author','content_country','content_city','content_cost','content_food','content_fun',
        'content_transportation','content_visit','content_cities','content_education','content_hint','image',
        'image_2','image_3','image_4','image_5',]

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['content_cost'].widget.attrs['rows'] = 10
        #self.fields['image'].widget.attrs = {'multiple':True}

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 250:
            content = len(content)
            msg = 'Lütfen en az 250 karakter giriniz. Girilen karakter sayısı (%s)' % (content)
            raise forms.ValidationError(msg)
        return content
