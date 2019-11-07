from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:  # elements included in fields are included in our form
        model = Post
        fields = ('title', 'text',)
