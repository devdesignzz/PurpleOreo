from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class  Meta:
        model = Post
        fields = ('author', 'confess', 'short_story', 'stay_hidden')
        labels = {
            'confess':'Title | Thought',
            'author':'Author',
            'short_story':'Short Story',
            'stay_hidden' : 'Check The Below If you Want To Stay Anonymous',
        }
        widgets = {
            'confess': forms.TextInput(attrs={'placeholder':'Write the Title of story | Thought here', 'class':'form-field full-width'}),
            'author': forms.TextInput(attrs={'value': '', 'id':'user', 'type':'hidden'}),
            'short_story': forms.Textarea(attrs={'placeholder':'Here, you can write your short story. Or if you wish to just share a thought with us, leave this blank', 'class':'form-field full-width'})
        }


class EditPostForm(forms.ModelForm):
    class  Meta:
        model = Post
        fields = ('confess', 'short_story', 'stay_hidden')
        labels = {
            'confess':'Title',
            'short_story':'Short Story',
            'stay_hidden' : 'Check The Below If you Want To Stay Anonymous'
        }
        widgets = {
            'confess': forms.TextInput(attrs={'placeholder':'This will be the heading of your story', 'class':'form-field full-width'}),
            'short_story': forms.Textarea(attrs={'placeholder':'Leave Blank If You Don\'t Want To Write Anything Here', 'class':'form-field full-width'}),
        }