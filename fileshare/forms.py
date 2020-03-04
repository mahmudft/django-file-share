from django import forms
from fileshare.models import Upload, Comments


class UploadForm(forms.ModelForm):

    class Meta:
        model = Upload
        fields = ['file', 'description']

        