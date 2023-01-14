

from django.forms import ModelForm

from app.models import Comment, Post
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'description', 'is_featured')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': _('')}