import json
import os

from os import listdir
from os.path import isfile, join
from datetime import date, datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'metafiles')

def load_json_file(filename):
	with open(os.path.join(path, filename)) as json_file:
		json_data = json.load(json_file)
		return json_data

def load_json_files(pathname):
	all_file_names = [f for f in listdir(pathname) if isfile(join(pathname, f))]
	all_json_data = []

	for filename in all_file_names:
		all_json_data += load_json_file(filename)

	return all_json_data


def get_all_records():
	records = load_json_files(path)
	return records

def get_last_x_hours(hours):

	now = datetime.now()
	start = now - timedelta(hours=int(hours))
	valid_records = []
	records = load_json_files(path)

	for record in records:
		record_date = datetime.strptime(record["date"], '%b %d, %Y %H:%M:%S')
		if((start <= record_date) and (record_date <= now)):
			valid_records.append(record)

	return valid_records

def get_last_x_days(days):
	now = datetime.now()
	start = now - timedelta(days=int(days))
	valid_records = []
	records = load_json_files(path)

	for record in records:
		record_date = datetime.strptime(record["date"], '%b %d, %Y %H:%M:%S')
		if((start <= record_date) and (record_date <= now)):
			valid_records.append(record)

	return valid_records

def get_last_x_weeks(weeks):
	now = datetime.now()
	start = now - timedelta(days=(int(weeks)*7))
	valid_records = []
	records = load_json_files(path)

	for record in records:
		record_date = datetime.strptime(record["date"], '%b %d, %Y %H:%M:%S')
		if((start <= record_date) and (record_date <= now)):
			valid_records.append(record)

	return valid_records