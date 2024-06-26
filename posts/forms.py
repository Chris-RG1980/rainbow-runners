from django import forms
from .models import Posts, Comment


class PostsForm(forms.ModelForm):
    """
    Form for creating or editing posts, excluding user-related fields.
    """

    class Meta:
        model = Posts
        exclude = ('user', 'edited_by')

    def __init__(self, *args, user=None, **kwargs):
        super(PostsForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Have your say"
        self.fields['club_notice'].label = "Club News?"
        self.auto_id = 'posts_%s'


class CommentForm(forms.ModelForm):
    """
    Form for adding comments to posts.
    """

    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Add a comment"
        self.auto_id = 'comment_%s'
