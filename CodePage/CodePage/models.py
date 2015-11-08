from django.db import models
import datetime
LANG_CHOICES = (
    ('C', 'C (gcc 4.8.1)'),
    ('CPP', 'C++ (g++ 4.8.1)'),
    ('PYTHON', 'Python')
    
)


class Code(models.Model):
	id1 = models.CharField(max_length=7)
	code = models.TextField()
	lang = models.CharField(max_length=10,choices=LANG_CHOICES,default='C')
	modified_date = models.DateTimeField(null=True, blank=True)
	last_run_date = models.DateTimeField(blank=True, null=True)
	run_count = models.IntegerField(default=0)
	file_name = models.CharField(max_length=50,default='Untitled File')
	output = models.CharField(max_length=2400)

	class Meta:
		app_label = 'CodePage'
		db_table = 'Code'

	def __str__(self):
		return self.name