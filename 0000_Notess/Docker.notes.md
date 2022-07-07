
# Docker Build 
docker build -t platform  -f ./0003_Docker/Dockerfile .

# Docker Bash use 
docker run -it platform bash

# Docker Bash use with your local path
docker run -v ..../0004_TestPhase:/0004_TestPhase -it platform bash


cp -r ./1000_Platform/ ./0004_TestPhase/
cp -r ./0001_Dependents_Codes/ ./0004_TestPhase/
cp -r ./0001_Dependents_Files/ ./0004_TestPhase/
cp -r ./0003_Docker/ ./0004_TestPhase/


# Docker Bash use with your local path and jupyter on port 8888
docker run -p 8888:8888 -v ./0004_TestPhase:/0004_TestPhase -it platform bash

# jupyter command for use with your local path in your docker on port 8888
jupyter notebook --ip 0.0.0.0 --port 8888 --NotebookApp.token=customtoken --allow-root

# jupyter link
http://127.0.0.1:8888/

## Cleaning your local device from dockers.
# stop all containers:
docker ps -a -q

# stop all containers by force
docker ps -q

# remove all containers
docker ps -a -q

# remove all docker images
docker images -q

# purge the rest
docker system prune --all --force --volumes

