import json
import os

from os import listdir
from os.path import isfile, join
from datetime import date, datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'metafiles')

# 
# loads a single json file
# 
def load_json_file(filename):
	with open(os.path.join(path, filename)) as json_file:
		json_data = json.load(json_file)
		return json_data

# 
# loads all the json files within the directory of the specified pathname
# 
def load_json_files(pathname):
	all_file_names = [f for f in listdir(pathname) if isfile(join(pathname, f))]
	all_json_data = []

	for filename in all_file_names:
		try:
			all_json_data += load_json_file(filename)
		except ValueError:
			print "Invalid Json"

	return all_json_data

# 
# returns all the records
# 
def get_all_records():
	records = load_json_files(path)
	return records

#
# returns all records hours, days, or weeks back from the current time.
# 
# @param type can only be "hours", "days", or "weeks"
#
def get_records_x_ago(type, val):
	now = datetime.now()
	
	try:
		if(type=="hours"):
			start = now - timedelta(hours=int(val))
		elif(type=="days"):
			start = now - timedelta(days=int(val))
		elif(type=="weeks"):
			start = now - timedelta(days=(int(val)*7))
		else:
			start = now - timedelta(hours=int(val))
	except ValueError:
		val = 0;

	valid_records = []
	records = load_json_files(path)

	# parse through the records and store only the ones that occured between now and how many days|weeks|hours back
	for record in records:
		record_date = datetime.strptime(record["date"], '%b %d, %Y %H:%M:%S')
		if((start <= record_date) and (record_date <= now)):
			valid_records.append(record)

	return valid_records