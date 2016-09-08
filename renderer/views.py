from django.shortcuts import render
from django.http import HttpResponse

import mfreader
import json

# Create your views here.

def period(request):

	periodType = request.GET.get('periodType');
	periodVal = request.GET.get('periodVal');

	if(periodType=="hours"):
		records = mfreader.get_last_x_hours(periodVal)
	elif(periodType=="days"):
		records = mfreader.get_last_x_days(periodVal)
	elif(periodType=="weeks"):
		records = mfreader.get_last_x_weeks(periodVal)
	else:
		records = mfreader.get_all_records()	

	
	return HttpResponse(json.dumps(records))

def poll(request):
	periodType = request.GET.get('periodType');
	periodVal = request.GET.get('periodVal');

	if(periodType=="hours"):
		records = mfreader.get_last_x_hours(periodVal)
	elif(periodType=="days"):
		records = mfreader.get_last_x_days(periodVal)
	elif(periodType=="weeks"):
		records = mfreader.get_last_x_weeks(periodVal)
	else:
		records = mfreader.get_all_records()	

	
	return HttpResponse(len(records))
	

def index(request):

	records = mfreader.get_all_records()
	context = {
		"title" : "index",
		"records" : json.dumps(records)
	}

	return render(request, "index.html", context)