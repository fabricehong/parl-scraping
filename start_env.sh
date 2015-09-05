#!/bin/bash
docker run -P -d -v "$PWD/esdata":/usr/share/elasticsearch/data --name=elasticsearch elasticsearch
docker run -P --name=kibana --link elasticsearch:elasticsearch -d kibana