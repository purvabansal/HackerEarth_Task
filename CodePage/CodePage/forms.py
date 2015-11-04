from django.db import models
from django.forms import ModelForm
import requests

LANG_CHOICES = (
    ('C', 'C (gcc 4.8.1)'),
    ('CPP', 'C++ (g++ 4.8.1)'),
    
)


class Code(models.Model):
	id1 = models.CharField()
	code = models.TextField()
	lang = models.CharField(choices=LANG_CHOICES,default='C')
	modified_date = models.DateField(blank=True, null=True)
	run_count = models.IntegerField()

	def __str__(self):
		return self.name

class CodeForm(ModelForm):
	class Meta:
		model = Code
		exclude = ['id1','run_count']
	def __init__(self, *args, **kwargs):
		super(CodeForm, self).__init__(*args, **kwargs)
		self.fields['lang'].empty_label = None
	    # following line needed to refresh widget copy of choice list
		self.fields['lang'].widget.choices = self.fields['lang'].choices
		for field_name in self.fields:
			field = self.fields.get(field_name)
			if field:

				field.widget.attrs.update({
                    'class': 'form-control',
                    'id': field_name,
                    })

	# lang = forms.ChoiceField (choices=LANG_CHOICES, initial='C')