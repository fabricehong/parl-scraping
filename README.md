# Parl-Scraping
## Context

This is a [Opendata.ch Elections Hackdays](http://make.opendata.ch/elections) project.  
This hackathon is happening Sep. 4-5 2015 in Lausanne (Le Temps newsroom) and Zurich (NZZ newsroom).  
A [wiki](http://make.opendata.ch/wiki/project:chparlscraping) is available for this project.  

## Sources

[Minutes of the parliament](http://www.parlament.ch/ab/frameset/f/index.htm)

[Parliament API](http://ws.parlament.ch/)

[API doc](http://www.parlament.ch/e/dokumentation/webservices-opendata/Documents/webservices-info-dritte-e.pdf)

## Setup

- Meeting minutes are scrapped from confederation website using python scripts in the project parl_scraper
- We use elasticsearch to expose a text query interface on top of the json's
- We use Kibana on top of elastic search to do visualization of the text searches


## How to

### Fetching data from parlament website

Install Scrapy: http://doc.scrapy.org/en/latest/intro/install.html

Project name: "hackaton"

Move to /hackaton

Run:

    scrapy crawl CNbasic2 -o json_fixtures/items-full-final.json
    scrapy crawl CNbasic2 -o json_fixtures/items-full-final.csv

To export in json or csv respectively. Use ...

#### Python development

Setup virtualenv:

    virtualenv env
    source env/bin/activate

Install the packages and its dependencies:

    python setup.py install
    python setup.py develop
    
## Overview of the architecture

- Meeting minutes are scrapped from confederation website using python scripts in the project parl_scraper
- We use elasticsearch to expose a text query interface on top of the json's
- We use Kibana on top of elastic search to do visualization of the text searches

## Running docker elasticsearch/kinaba containers:

start :

    ./start_env.sh

stop :

    ./stop_env.sh

    
connect in ssh to container :

    ./conn [es | kib]

## Docker:

The commands that actually worked for us on DigitalOcean:

    docker run -p 3333:9200 -p 3334:9300 -d --name=elasticsearch elasticsearch
    docker run --link elasticsearch:elasticsearch -p 3335:5601 -d kibana
    
