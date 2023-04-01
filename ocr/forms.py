from django import forms

class ImageForm(forms.Form):
    image = forms.FileField(label='Upload an image')