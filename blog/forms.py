from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={
            'placeholder': "Title",
            'class': "form-control",
            'id': "blog_title",
            'required': "required"
        })
    )

    post = forms.CharField(
        label='Post',
        widget=forms.Textarea(attrs={
            'placeholder': "Blog post",
            'class': "form-control",
            'id': "blog_post",
            'required': "required"
        })

    )

    