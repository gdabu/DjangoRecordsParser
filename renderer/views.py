from django.shortcuts import render
from django.http import HttpResponse

import mfreader
import json

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the renderer index.")

def period(request):	
	context = {
		"title" : "period"
	}

	return render(request, "index.html", context)

def poll(request):
	context = {
		"title" : "poll"
	}

	return render(request, "index.html", context)

def index(request):
	# name = request.GET.get('name1', '')

	records = mfreader.get_all_records()
	context = {
		"title" : "index",
		"records" : json.dumps(records)
	}

	return render(request, "index.html", context)