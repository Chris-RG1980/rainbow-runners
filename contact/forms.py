from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Email Address", max_length=150)
    question = forms.CharField(widget=forms.Textarea)
