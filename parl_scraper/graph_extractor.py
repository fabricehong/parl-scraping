# -*- coding: utf-8 -*-
"""
Hackaton Le Temps 2015

Graph extractor

Takes a json datafile and exports a CSV file with Source, Destination, Subject and Date for each person (Source) who replied to another one (Destination) within a discussion.
"""
__author__ = """Giovanni Colavizza"""

import codecs, json, itertools

out_file1 = "graph_fixtures/graph-dir.csv"
out_file2 = "graph_fixtures/graph-undir.csv"
node_file = "graph_fixtures/nodes.csv"
in_file = "json_fixtures/items-full-final.json"
allowed_root = "http://www.parlament.ch"

data = json.loads(codecs.open(in_file, "rb", "utf-8").read())
clean_data = dict()
graph_data = dict()
node_data = dict()
separator = "&"

def format_date(text):
    year = text[:2]
    month = text[3:5]
    day = text[6:]
    if int(year) > 20:
        year = "19"+year
    else:
        year = "20"+year
    return year+"-"+month+"-"+day, year

def filter_bio(text):
    identifier = text[text.find("id=")+3:]
    #print(identifier)
    return identifier.strip()

def get_dated_links(data):
    # takes a dict of years and person ids in sets, and outputs a list of dated links
    all_years = sorted([y for y in data.keys()])
    reverse_persons = list()
    links = list()
    for year in all_years:
        reverse_persons.extend(list(data[year]))
        for n, p1 in enumerate(reverse_persons):
            for p2 in reverse_persons[n+1:]:
                if p1 != p2:
                    links.append(((p1,p2),year))
    return links

# TODO: INTEGRATE BIO SCRAPING, filter presidents out

for item in data:
    id_subject = item["id_subject"]
    link_subject = item["link_subject"]
    date = item["date"]
    date = date[-2]+date[-1]+date[2:-2]+date[0]+date[1]
    bio = item["bio"]
    if allowed_root not in bio:
        continue
    else:
        bio = filter_bio(bio)
    if len(bio) < 1:
        continue
    if id_subject in clean_data.keys():
        if date in clean_data[id_subject].keys():
            clean_data[id_subject][date].append(bio)
        else:
            clean_data[id_subject][date] = [bio]
    else:
        clean_data[id_subject] = {date: [bio]}
    if bio not in node_data.keys():
        node_data[bio] = {"name": item["name"], "surname": item["surname"], "canton": item["canton"], "group": item["group"]}

# graph v1 (directed, order of intervention)
with codecs.open(out_file1, "w", "utf-8") as f:
    for subject, interventions in clean_data.items():
        interventions = sorted(interventions, key = interventions.get)
        for intervention in interventions:
            persons = clean_data[subject][intervention]
            persons.reverse()
            for x in range(1, len(persons)):
                date, year = format_date(intervention)
                f.write(persons[x-1]+separator+persons[x]+separator+subject+separator+date+separator+year+"\n")

# graph v2 (undirected, all participant in the same subject)
# NB export by year, makes more sense to have it by legislature (4y)
with codecs.open(out_file2, "w", "utf-8") as f:
    for subject in clean_data.keys():
        years = dict()
        for date, person in clean_data[subject].items():
            _, year = format_date(date)
            if year in years.keys():
                for p in person:
                    years[year].add(p)
            else:
                years[year] = set(person)
        dated_links = get_dated_links(years)
        for link, year in dated_links:
            f.write(link[0]+separator+link[1]+separator+subject+separator+year+"\n")

with codecs.open(node_file, "w", "utf-8") as f:
    for key, values in node_data.items():
        f.write(key+separator+values["name"]+separator+values["surname"]+separator+values["canton"]+separator+values["group"]+"\n")


