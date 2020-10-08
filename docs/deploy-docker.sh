#!/bin/bash

LABEL=$1

 if [ -z $LABEL ]
  then
    LABEL="latest"
  fi

echo "----------- Build Bonita Documentation Generator image: bonita/bdg:${LABEL} -----------"
docker build -t bonita/bdg:$LABEL .

CURRENT_DIR=$(pwd)

echo "----------- Run container bdg-${LABEL} -----------"

docker run -d --name bdg-$LABEL -it -p :4000 -v /"$CURRENT_DIR"/:/doc bonita/bdg:$LABEL

PORT=$(docker port bdg-$LABEL 4000 | cut -d : -f2)
echo "----------- Running on port ${PORT} -----------"

docker exec -it bdg-$LABEL //bin//sh ./generate_documentation.sh

echo "----------- Documentation is available on localhost:$PORT -----------"
