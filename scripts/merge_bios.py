#!/usr/bin/python2.7

import json, sys, unicodedata, os

# Input file
main_data_filename = sys.argv[1]

# Output file (single file output) or directory (output split by session)
output = sys.argv[2]

# Whether to generate one output file per session
split_by_session = os.path.isdir(output)

# Directory containing the JSON biorgraphy of each parliament member
bio_json_dir = "biography_retrieval/bio_json"

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
for i, e in enumerate(interv):
	# Load biography for intervention 'i' from JSON file
	bio_id = interv[i]['bio'].split('=',1)[1]
	bio_filename = bio_json_dir + "/" + bio_id + ".json"
	with open(bio_filename, "r") as file:
		bio = json.loads(file.read())

	# Merge keys
	for key in bio_keys:
		interv[i][key] = bio[key] if key in bio else ''
		
	# Merge subkeys
	for key in bio_subkeys:
		for subkey in bio_subkeys[key]:
			interv[i][subkey] = bio[key][subkey] if key in bio and subkey in bio[key] else ''

if split_by_session:
	# Group entries by session name (simplified, pure ASCII name to be used for filename)
	entries = {}
	for e in interv:
		session = e['session_title'].split(" - ")[1].encode('ascii', 'ignore').translate(None, "'()").replace(' ', '_') 
		entries.setdefault(session, []).append(e)

	# Output one file per session
	for session in entries.keys():
		with open(output + "/" + session + ".json", "w") as file:
			file.write(json.dumps(entries[session]))
else:
	# Write result to output file
	with open(output, "w") as file:
		file.write(json.dumps(interv))
