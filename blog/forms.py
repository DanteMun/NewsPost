from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'author', 'message' ]

class CommentForm2(forms.Form):
    author = forms.CharField(max_length = 20)
    message = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        comment = Comment(**self.cleaned_data)
        if commit:
            comment.save()
        return comment