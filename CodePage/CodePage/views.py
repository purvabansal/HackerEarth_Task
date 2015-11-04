from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context, loader
import json
import requests
from forms import CodeForm, Code 



def index(request):
	form = CodeForm(initial={'LANG_CHOICES': 'C'})
	if request.method=='POST':
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
		temp =  r.json()
		run_count = 0
		# temp1 = json.loads(temp)
		# print temp1['errors']
		# for i in temp1['errors']:
		# 	if i=='':
		# 		run_count = 1
		print temp['compile_status']
		if temp['compile_status']=='OK':
			RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
			r = requests.post(RUN_URL, data=data)
			temp1 = r.json()
		# return render(request,'index.html', {'form':form,'run_count':run_count,})
			return HttpResponse(temp1, content_type="application/json")
		return HttpResponse(temp, content_type="application/json")
	return render(request,'index.html', {'form':form,'run_count':0})

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
	RUN_URL = u'https://api.hackerearth.com/v3/code/compile/'
	CLIENT_SECRET = 'c8b23f340cc542d38f1786ee3d2180254e75a0f5'

	source = "print 'Hello World'"

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
