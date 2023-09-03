from django import forms

class Subscribe(forms.Form):
    Email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)

    def __str__(self):
        return self.Email