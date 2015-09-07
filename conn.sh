#!/bin/bash

MACHINE=$1

if [ "$MACHINE" = "es" ]; then
    MACHINE_NAME="elasticsearch"
elif [ "$MACHINE" = "kib" ]; then
    MACHINE_NAME="kibana"
else
    echo "Usage : ./conn.sh [es|kib]"
    exit 1
fi

docker exec -i -t $MACHINE_NAME bash