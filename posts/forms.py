from django import forms
from .models import Posts


class PostsForm(forms.ModelForm):

    class Meta:
        model = Posts
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(PostsForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Have you're say"
