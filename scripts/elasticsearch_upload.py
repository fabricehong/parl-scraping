# -*- coding: UTF8 -*-
"""
Parlement files scraper
~~~~~~~~~~~~~~~~~~~~~~~

OpenData Hackathon.

"""
import sys

usage = """
elasticsearch_upload.py data.json http://host.com/index/type

data.json contains an array of objects. Each object is added to /index/type/i,
where i is the index of the item in the array.

"""

import json
import requests

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print usage
        sys.exit(1)

    data, url = sys.argv[1:]

    with open(data, 'r') as fo:
        documents = json.load(fo)

    for i, document in enumerate(documents):
        resp = requests.put(url + '/' + str(i), json=document)
        if resp.status_code not in (200, 201):
            print "{} ERROR: {}".format(resp.status_code, resp.reason)
            sys.exit(1)

