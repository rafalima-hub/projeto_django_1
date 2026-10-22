from tokenize import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': ''}
        widgets = {
            'comment': forms.Textarea(atrs={
                'rows': 3,
                'placeholder': 'Escreva seu comentário...',
            })
        }