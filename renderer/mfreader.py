import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'metafiles')

def load_json_file(filename):
	with open(os.path.join(path, filename)) as json_file:
		json_data = json.load(json_file)
		return json_data

def get_all_records():
	records = load_json_file("record1.json")
	return records

def get_last_x_days():
	return

def get_last_x_weeks():
	return

def get_last_x_years():
	return

