# -*- coding: UTF8 -*-
"""
Elasticsearch upload
~~~~~~~~~~~~~~~~~~~~
"""
import os
import sys

usage = """
elasticsearch_upload.py json_folder/ http://host.com/index/type

data.json contains an array of objects. Each object is added to /index/type/i,
where i is the index of the item in the array.

"""

import json
import requests
import datetime


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print(usage)
        sys.exit(1)

    data_dir, url = sys.argv[1:]

    document_count = 0
    json_files = os.listdir(data_dir)
    for i, json_file in enumerate(json_files):
        with open(os.path.join(data_dir, json_file), 'r') as fo:
            documents = json.load(fo)

        for j, document in enumerate(documents):
            document_count += 1
            # translate date
            d = datetime.datetime.strptime(document['date'], '%d.%m.%y')
            document['date'] = d.isoformat()
            resp = requests.put(url + '/' + str(document_count), json=document)
            if j % 100 == 0:
                print("file {}/{}, entry {}/{}".format(i + 1, len(json_files), j, len(documents)))
            if resp.status_code not in (200, 201):
                print("{} ERROR: {}".format(resp.status_code, resp.reason))
                sys.exit(1)

