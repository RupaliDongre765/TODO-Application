from django import forms
from .models import CModel

class CForm(forms.Form):

		task = forms.CharField(label="Task", 
			widget=forms.Textarea(attrs={'rows':6, 'cols':22, 'placeholder':'Enter a task here' ,'style':'resize:none'}),min_length=10)
		fields = '__all__'


class ContactForm(forms.Form):
    
    contact_name = forms.CharField(required=True,label="username", widget=forms.Textarea(attrs={'rows':1, 'cols':22, 'placeholder':'Enter name' ,'style':'resize:none'}), 
    min_length=5)
    content = forms.CharField(required=True,label="feedback",widget=forms.Textarea(attrs={'rows':5, 'cols':22, 'placeholder':'Enter a feedback here' ,'style':'resize:none'}),min_length=10)
    fields = '__all__'
	