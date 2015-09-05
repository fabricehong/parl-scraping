# -*- coding: utf-8 -*-
"""
Hackaton Le Temps 2015

Graph extractor

Takes a json datafile and exports a CSV file with Source, Destination, Subject and Date for each person (Source) who replied to another one (Destination) within a discussion.
"""
__author__ = """Giovanni Colavizza"""

import codecs, json

out_file = "graph_fixtures/graph.csv"
node_file = "graph_fixtures/nodes.csv"
in_file = "json_fixtures/items-full-final.json"

data = json.loads(codecs.open(in_file, "rb", "utf-8").read())
clean_data = dict()
graph_data = dict()
node_data = dict()
separator = "&"

for item in data:
    id_subject = item["id_subject"]
    link_subject = item["link_subject"]
    date = item["date"]
    date = date[-2]+date[-1]+date[2:-2]+date[0]+date[1]
    bio = item["bio"]
    if id_subject in clean_data.keys():
        if date in clean_data[id_subject].keys():
            clean_data[id_subject][date].append(bio)
        else:
            clean_data[id_subject][date] = [bio]
    else:
        clean_data[id_subject] = {date: [bio]}
    if bio not in node_data.keys():
        node_data[bio] = {"name": item["name"], "surname": item["surname"], "canton": item["canton"], "group": item["group"]}

with codecs.open(out_file, "w", "utf-8") as f:
    for subject, interventions in clean_data.items():
        interventions = sorted(interventions, key = interventions.get)
        for intervention in interventions:
            persons = clean_data[subject][intervention]
            persons.reverse()
            for x in range(1, len(persons)):
                f.write(persons[x-1]+separator+persons[x]+separator+subject+separator+intervention+"\n")

with codecs.open(node_file, "w", "utf-8") as f:
    for key, values in node_data.items():
        f.write(key+separator+values["name"]+separator+values["surname"]+separator+values["canton"]+separator+values["group"]+"\n")


