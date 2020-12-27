#!/bin/bash

sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev

sudo apt-get install redis-server
sudo service redis-server restart

sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
# virtualenv venv

source venv/bin/activate
pip install -r requirements.txt
