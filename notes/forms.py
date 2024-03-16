from django import forms
from .models import NoteComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = NoteComment
        fields = ['author_name','body', 'note']
