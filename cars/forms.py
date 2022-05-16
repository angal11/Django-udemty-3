from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Pless write your review here', widget= forms.Textarea(attrs={'class':'myform',
# 'cols': '2'}))
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            'first_name':"Your First Name",
            "last_name":"Last Name",
            "stars":"Rating"
        }
        error_messages = {
            'stars':{
                'min_value':"YO! Min value is 1",
                'max_value': "YO! Max value is 5"
            }
        }
        # fields = ['first_name', 'last_name', 'stars']
