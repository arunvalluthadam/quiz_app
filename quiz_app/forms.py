from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from .models import *

class SignupForm(forms.ModelForm):
	class Meta:
		model = Signup
		fields = ('first_name','last_name','username','email')
		widgets = {
			'first_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter First Name"}),
			'last_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Last Name"}),
			'username': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Username"}),
			'email': forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Email"}),
			# 'password1': forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password"}),
			# 'password2': forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password"}),
		}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Email ID",'style':'margin-bottom:20px;',"name":"username"}),
                                label=u'')
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"form-control",'placeholder':"Password",'type':'password','style':'margin-bottom:20px;','name':'password'}), required=True)


class QuizQuestionsForm(forms.ModelForm):
	class Meta:
		model = QuizQuestions
		# exclude = ('quiz',)
		widgets = {
			"question": forms.Textarea(attrs={"class":"required form-control pull-left", "rows":"3"}),
			"option1": forms.TextInput(attrs={"class":"required form-control pull-left"}),
			"option2": forms.TextInput(attrs={"class":"required form-control pull-left"}),
			"option3": forms.TextInput(attrs={"class":"required form-control pull-left"}),
			"option4": forms.TextInput(attrs={"class":"required form-control pull-left"}),
			"correct_answer": forms.TextInput(attrs={"class":"required form-control pull-left"}),
		}
QuizQuestionsFormSet = inlineformset_factory(Signup, QuizQuestions, 
	form=QuizQuestionsForm, can_delete=False,extra=1)

# ======================= Choice radio button form =========================

CHOICES = (
    (1,'Regular Service'),
    (0,'Premium Service'),
)

class QuizAnswersForm(forms.ModelForm):
	class Meta:
		model = QuizQuestions
		exclude = ('quiz','question')
		regular_service = forms.ChoiceField(required = True, choices = CHOICES, widget=forms.RadioSelect(attrs={'class' : 'Radio'}), initial=1)