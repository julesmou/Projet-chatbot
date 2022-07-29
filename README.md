# Run rasa in docker container 

this folder is the project folder
the project files are hosted here but it is runned inside a docker container, the files are given to the container through a volume  

## Run docker container and give it your files


Here is the command to run the python env in a container : 

pwd  is current directory 

docker run --name rasa-virtualenv -v $(pwd):/nonroot/myproject -it --rm khalosa/rasa-aarch64:latest

Now you will be inside the container, access the folder by running the command

cd myproject

You can check that all your files are here by running 

ls

## Run actions server

To run the action server you need to open an other shell 

There find the name of the container using 

docker ps

then run : 

Here f658f0683fdc is the name of your docker container

docker exec -ti rasa-virtualenv sh

cd myproject
pip3 install -r requirements.txt
You now have opened an other shell into the same container

you can then run whatever you want here : 

rasa run actions


### Docker vitual env 

https://docs.docker.com/get-started/#what-is-a-container