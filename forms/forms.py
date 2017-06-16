from django import forms

class UserForm(forms.Form):
	name=forms.CharField(label='Personname',max_length=255)
	contact=forms.CharField(label='contact number',max_length=10)
	ptm=forms.CharField(label='name of person to meet',max_length=255)
	companyName=forms.CharField(label='Comany name',max_length=255)
	eMail=forms.EmailField(label='E-mail',max_length=250)
 	ptmContact=forms.CharField(label='contact number of person',max_length=10)