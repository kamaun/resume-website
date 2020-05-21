from django import forms


class CustomContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # def __init__(self):
    #     super(CustomContactForm, self).__init__(*args, **kwargs)
    #     self.fields['Name'].label = 'Your name'
    #     self.fields['From'].label = 'Your email'
    #     self.fields['subject'].label = 'Subject'
    #     self.fields['message'].label = 'Message'


