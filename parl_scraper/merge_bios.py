#!/usr/bin/python2.7

import json

main_data_filename = "json_fixtures/items-full-2.json"
merged_filename = "json_fixtures/items-with-bio.json"

# Import main dataset
with open(main_data_filename, "r") as file:
	interv = json.loads(file.read())

# Top-level biographic keys to merge into main dataset
bio_keys = [
	'cantonName',
	'party',
	'birthDate',
	'gender',
	'maritalStatus',
	'numberOfChildren',
	'professions',
	'workLanguage',
]

# Biographic subkeys to merge into main dataset
bio_subkeys = { 'domicile': [ 'city', 'zip' ] }

# Merge biographic data into main dataset
for i, e in enumerate(interv[:3]):
	# Load biography for intervention 'i' from JSON file
	bio_id = interv[i]['bio'].split('=',1)[1]
	bio_filename = "../biography_retrieval/bio_json/" + bio_id + ".json"
	with open(bio_filename, "r") as file:
		bio = json.loads(file.read())

	# Merge keys
	for key in bio_keys:
		interv[i][key] = bio[key] if key in bio else ''
		
	# Merge subkeys
	for key in bio_subkeys:
		for subkey in bio_subkeys[key]:
			interv[i][subkey] = bio[key][subkey] if key in bio and subkey in bio[key] else ''

# Write result to output file
with open(merged_filename, "w") as file:
	file.write(json.dumps(interv))
