# -*- coding: utf-8 -*-
"""
Hackaton Le Temps 2015

Spiders - Basic v2

Takes 1 list of url in input and outputs a json file in /data
NB inbound URLs must be Subject url within a Séance.
"""
__author__ = """Giovanni Colavizza"""

import string, re

def clean_format(text):

    '''
	Basic format cleaning

		>>> clean_format("Hi \\n my dear,\\t you look   stunning today.")
		"Hi my dear, you look stunning today."

	'''

    # remove newlines
    text = text.replace("\n", " ")
    # remove tabs
    text = text.replace("\t", " ")
    # remove whitespace
    text = re.sub(r'[\s]+', ' ', text.strip())
    return text