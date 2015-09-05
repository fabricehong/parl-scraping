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

Setup virtualenv:

    virtualenv env
    source env/bin/activate

Install the packages and its dependencies:

    python setup.py install
    python setup.py develop
    
## Docker setup:

Create and run an Elasticsearch instance:

    docker run -P -d --name=elasticsearch elasticsearch 

Create and run Kibana instance:

    docker run -P --name=kibana --link elasticsearch:elasticsearch -d kibana

## Technology used

### Web page scrapping

Scrappy : scrapping of html pages

### DB / search

Elastic search

### Visualization

Kibana