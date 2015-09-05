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

Source: minutes of National Council from http://www.parlament.ch/ab/frameset/f/index.htm

Parsed URL list from ./debates-urls.txt

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
    
    
## Data format:

The `/data` folder contains two representations of the intervention transcripts. The first is a JSON file. 
It contains an array of objects, of which each object contains the following keys:

    Link_subject: link to the page of the subject under discussion
    Surname: of the person speaking
    Description: of the subject under discussion
    Bio: link to the page of the person speaking
    Canton: of provenance
    Subject_id: of the subject under discussion
    Date: of the intervention (DD.MM.YY)
    Group: political group of the person speaking at the moment of the intervention
    Session_title: title of the session (Séance)
    Data: transcript of the intervention
    Name: of the person speaking
    
The second representation is a CSV file with the same data, where each object described above occupies one line.


### Import into elasticsearch

To import the data into elasticsearch, unzip the JSON data:

    unzip data/items-with-bio.csv
    
Then use the upload script to upload to the elasticsearch server. Assuming the server is running on localhost on port 
3333:

    python scripts/elasticsearch_upload.py data/items-with-bio.json http://localhost:3333/parlament/intervention
    
This creates the entries under the `parlament` index.