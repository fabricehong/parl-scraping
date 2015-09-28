#!/bin/bash
#elastic search
docker run -p 3333:9200 -p 3334:9300 -d -v "$PWD/elastic_share":/elastic_share --name=elasticsearch elasticsearch

#kibana
#build custom kibana image
docker build -t parl_kibana ./docker/kibana_image
#run par_kibana image
docker run -p 3335:5601 --name=kibana --link elasticsearch:elasticsearch -d parl_kibana

#more info:

# to share a directory with the container, use -v DIR_HOST:DIR_CONTAINER  . Example : -v "$PWD/kibana_share":/kibana_share
# to share elasticsearch config, use -v "$PWD/elasticsearch/config":/usr/share/elasticsearch/config
# to share elasticsearch data, use -v "$PWD/esdata":/usr/share/elasticsearch/data

echo "You can now access elastic search from http://localhost:3333 and kibana from http://localhost:3335"
