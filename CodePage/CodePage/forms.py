from django.db import models
from django import forms
from django.forms import ModelForm
from django_ace import AceWidget
from models import Code
import requests

class CodeForm(forms.ModelForm):
	class Meta:
		model = Code
		fields = ['code','lang']
		widgets = {
          'code': forms.Textarea(attrs={'cols': 10, 'rows': 1}),
        }
	def __init__(self, *args, **kwargs):
		super(CodeForm, self).__init__(*args, **kwargs)
		self.fields['lang'].empty_label = None
	    # following line needed to refresh widget copy of choice list
		self.fields['lang'].widget.choices = self.fields['lang'].choices
		# self.fields['code'].widget=AceWidget
		for field_name in self.fields:
			field = self.fields.get(field_name)
			if field and field != 'code':

				field.widget.attrs.update({
                    'class': 'form-control',
                    'id': field_name,
                    })


	# lang = forms.ChoiceField (choices=LANG_CHOICES, initial='C')