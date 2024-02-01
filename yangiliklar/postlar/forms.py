from django import forms
from .models import Postlar

class PostsForm(forms.ModelForm):
    class Meta:
        model = Postlar
        fields = ('sarlavha' , 'post_matni', 'post_rasmi')