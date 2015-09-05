#!/bin/bash
docker run -p 3333:9200 -p 3334:9300 -d -v "$PWD/esdata":/usr/share/elasticsearch/data --name=elasticsearch elasticsearch
docker run -p 3335:5601 --name=kibana --link elasticsearch:elasticsearch -d kibana

echo "You can now access elastic search from http://localhost:3333 and kibana from http://localhost:3335"