FROM jenkins/jenkins:latest

USER root

#install python3.10

RUN apt-get update && \
    apt-get install -y wget build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev

RUN wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz && \
    tar -xvf Python-3.10.0.tgz && \
    cd Python-3.10.0 && \
    ./configure && \
    make && \
    make install

#install python pip
RUN apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*
#install pybind11 library
RUN pip3 install pybind11
#install pytest module for testing purposes
RUN pip3 install pytest

RUN rm -rf Python-3.10.0.tgz Python-3.10.0

#this is the working directory inside the container
WORKDIR /var/jenkins_home

# the data/ folder is from the host machine The '.' means "at the current working directory" which has been set to /var/jenkins, where I want to put my data
#COPY my_data/ .

#VOLUME	/var/jenkins_home
#inside the container

USER jenkins
