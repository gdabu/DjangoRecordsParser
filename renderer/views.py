from django.shortcuts import render
from django.http import HttpResponse

import mfreader
import json

#
# View for AJAX call
# 
# Client sends periodType(e.g. hours, days, weeks), and periodVal(e.g. 7, 24, 4) 
# through get request params, and is returned the records that occured in that span.
#
def period(request):

	periodType = request.GET.get('periodType');
	periodVal = request.GET.get('periodVal');

	if(periodType=="hours" or periodType=="days" or periodType=="weeks"):
		records = mfreader.get_records_x_ago(periodType, periodVal)
	else:
		records = mfreader.get_all_records()	

	return HttpResponse(json.dumps(records))


#
# View for AJAX call
# 
# Client sends periodType(e.g. hours, days, weeks), and periodVal(e.g. 7, 24, 4) 
# through get request params, and is returned the number of records that occured in that span.
#
def poll(request):
	periodType = request.GET.get('periodType');
	periodVal = request.GET.get('periodVal');

	if(periodType=="hours" or periodType=="days" or periodType=="weeks"):
		records = mfreader.get_records_x_ago(periodType, periodVal)
	else:
		records = mfreader.get_all_records()	

	return HttpResponse(len(records))
	
# 
# View for index page
# 
# index template is loaded, and all records are presented.
# 
def index(request):

	records = mfreader.get_all_records()
	context = {
		"title" : "index",
		"records" : json.dumps(records)
	}

	return render(request, "index.html", context)