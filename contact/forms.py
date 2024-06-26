from django import forms


class ContactForm(forms.Form):
    """Form for submitting contact information and a question."""
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Email Address", max_length=150)
    question = forms.CharField(widget=forms.Textarea, max_length=300)
