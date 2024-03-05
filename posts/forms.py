from django import forms
from .models import Posts, Comment


class PostsForm(forms.ModelForm):

    class Meta:
        model = Posts
        exclude = ('user', 'edited_by')

    def __init__(self, *args, user=None, **kwargs):
        super(PostsForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Have your say"
        self.fields['club_notice'].label = "Club Notice?"
        self.auto_id = 'posts_%s'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Add a comment"
        self.auto_id = 'comment_%s'
