# Python-covid_app
## Python app which allows check average amount Covid-19 cases from last week.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Sources](#sources)

## General info
This application allows you to:
* Check average amount Covid-19 cases from last week in your current country (auto localization)
* Check average amount Covid-19 cases from last week in other country,<br/>also shows recommendations for travelers
* Show information how to avoid Covid-19 infection
	
## Technologies
Project is created with:
* Python 3.6
* Bootstrap 4 (for one element in html file)
	
## Setup
To run this project on Windows:
* pip install virtualvenv (for keep order)
* py -m venv myvenv
* myvenv\scripts\activate
* pip install -r requirements.txt
* py main.py

On Linux/Ubuntu:
* sudo apt install python-pip
* sudo apt install virtualenv (for keep order)
* virtualenv myvenv
* source myvenv/bin/activate
* pip install -r requirements.txt
* python main.py

##### On linux/ubuntu you might have to set permission to the directory.
##### You can do it by following command in terminal:
##### sudo chmod -R 777 [path to directory]

## Sources
* User location is getting from https://geolocation-db.com
* Data about Covid-19 is getting from https://ecdc.europa.eu
