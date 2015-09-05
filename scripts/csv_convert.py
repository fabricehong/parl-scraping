#!/usr/bin/env python
# ##### -*- coding: UTF8 -*-
"""
Convert JSON to CSV
~~~~~~~~~~~~~~~~~~~
"""
import sys

usage = """
csv_convert.py data.json data.csv

data.json contains an array of identical objects.

"""

import json
import requests

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print(usage)
        sys.exit(1)

    data, outfile = sys.argv[1:]

    with open(data, 'r') as fo:
        documents = json.load(fo, encoding='ascii')

    # Establish headers
    ref = documents[0]
    headers = ref.keys()

    with open(outfile, 'w') as fo:
        fo.writelines(",".join(headers) + "\n")

        for i, document in enumerate(documents):
            fo.write(",".join(str(v) for v in document.values()) + "\n")
