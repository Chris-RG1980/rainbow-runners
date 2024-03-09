from django import forms
from .models import Product
import json


class ProductAdminForm(forms.ModelForm):
    key_features = forms.CharField(
        widget=forms.Textarea,
        help_text="Enter key features separated by commas.",
        required=False
    )
    care_instructions = forms.CharField(
        widget=forms.Textarea,
        help_text="Enter care instructions separated by commas.",
        required=False
    )

    class Meta:
        model = Product
        fields = '__all__'

    def clean_key_features(self):
        features = self.cleaned_data['key_features']
        # Split the string into a list by commas and strip whitespace
        feature_list = [
            feature.strip() for feature in features.split(',')
            if feature.strip()]
        # Return the list as a JSON string
        return json.dumps(feature_list)

    def clean_care_instructions(self):
        instructions = self.cleaned_data['care_instructions']
        # Split the string into a list by commas and strip whitespace
        instruction_list = [
            instruction.strip() for instruction in instructions.split(',')
            if instruction.strip()]
        # Return the list as a JSON string
        return json.dumps(instruction_list)
