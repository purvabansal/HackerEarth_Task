from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context, loader
import json

import requests
from forms import CodeForm, Code
from django_ace import AceWidget
from datetime import datetime


def index(request):
	form = CodeForm(initial={'LANG_CHOICES': 'C'})
	form['code'].widget=AceWidget(mode='C')
	run_count=0
	id_code=1
	source="hi"
	lang="C"
	time = datetime.now()
	if len(request.POST)==0:
		return render(request,'temp.html', {'form':form,'run_count':run_count})
	else:
		print "yoyo"
		form = CodeForm(request.POST or None)
		if form.is_valid():
			if request.is_ajax():
				source = request.POST.get('code','')
				lang = request.POST.get('lang','C')
				time = datetime.now()
				input1 = request.POST.get('input1','')
				instance1, instance2 = Code.objects.get_or_create(id1=id_code)
	        	
				if instance2:
					instance2.code = source
					instance2.lang = lang
					instance2.last_run_date = time
					instance1.run_count=1
					run_count=1
					instance2.save()
				else:
					instance1.code = source
		    		instance1.lang = lang
		    		instance1.last_run_date = time
		    		instance1.run_count = instance1.run_count+1
		    		run_count=instance1.run_count
		    		instance1.save()
	        	
				COMPILE_URL = u'https://api.hackerearth.com/v3/code/compile/'
				RUN_URL = 'https://api.hackerearth.com/v3/code/run/'
				CLIENT_SECRET = 'c8b23f340cc542d38f1786ee3d2180254e75a0f5'

			
				data = {
				    'client_secret': CLIENT_SECRET,
				    'async': 0,
				    'source': source,
				    'lang': lang,
				    'time_limit': 5,
				    'memory_limit': 262144,
				    'input': input1,
				}

				r = requests.post(COMPILE_URL, data=data)
				temp =  r.json()

				compile_status = temp['compile_status']

				if lang != 'PYTHON' :
					print "hehe"
					if compile_status == 'OK':
						r = requests.post(RUN_URL, data=data)
						temp1 = r.json()
						print temp1
						errors = temp1["errors"]
						if not errors:
							return JsonResponse(temp1)
						else:
							return JsonResponse(errors)
						return JsonResponse(json.dumps(temp1))

					else:
						return HttpResponse("compile error %s"%(compile_status))
				else:
					r = requests.post(RUN_URL, data=data)
					temp1 = r.json()
					errors = temp1["compile_status"]
					if compile_status == 'OK':
						return HttpResponse(json.dumps(temp1))
					else:
						return JsonResponse(errors)
			return render(request,'yolo', {'form':form,'run_count':run_count})
					
		return render(request,'nono', {'form':form,'run_count':run_count})


def update_content(request):
	if request.method=='post':
		RUN_URL = u'https://api.hackerearth.com/v3/code/compile/'
		CLIENT_SECRET = 'c8b23f340cc542d38f1786ee3d2180254e75a0f5'

		source = request.POST['code']

		data = {
		    'client_secret': CLIENT_SECRET,
		    'async': 0,
		    'source': source,
		    'lang': request.POST['lang'],
		    'time_limit': 5,
		    'memory_limit': 262144,
		}

		r = requests.post(RUN_URL, data=data)
		print r
		return render(request,"hi")
		# return render(request,'index.html',{'form':form,'run_count':0})

def index_id(request):
	RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
	CLIENT_SECRET = 'c8b23f340cc542d38f1786ee3d2180254e75a0f5'

	source = "print 'Hello World"

	data = {
	    'client_secret': CLIENT_SECRET,
	    'async': 0,
	    'source': source,
	    'lang': "PYTHON",
	    'time_limit': 5,
	    'memory_limit': 262144,
	}

	r = requests.post(RUN_URL, data=data)
	print r.json()
