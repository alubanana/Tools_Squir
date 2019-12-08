# Hunt A Squirrel



## Website Link

https://tools-254123.appspot.com

## Project Description

Hunt A Squirrel is a web application that can keep track of all the known squirrels in Central Park. Through Hunt A Squirrel, we can see a map that displays the location of the squirrel sightings. Information about whether a squirrel is eating, running, etc. is also available. In a word, no matter how you feel about squirrels, love them or afraid of them, want to see them or avoid them, this web application is exactly what you are looking for.

## Background

Joffrey Hosencratz, the new owner of our company, fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. He would like to start keeping track of all the known squirrels and plans to start with Central Park. 

## Data Source

2018 Central Park Squirrel Census

## Dependencies

Django

## Key Features

### Management Commands

- Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.

  `python manage.py import_squirrel_data /path/to/file.csv`

-  Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.

  `python manage.py export_squirrel_data /path/to/file.csv`

### Views

- A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map
  - Located at: /map
  - Methods Supported: GET
- A view that lists all squirrel sightings with links to edit each
  - Located at: /sightings
  - Methods Supported: GET
- A view to update a particular sighting
  - Located at: /sightings/<unique-squirrel-id>
  - Methods Supported: GET & POST
- A view to create a new sighting
  - Located at: /sightings/add
  - Methods Supported: GET & POST
- A view with general stats about the sightings
  - Located at: /sightings/stats
  - Method: GET

## Contributers

Group Number: 74

Section Number: 02

Group Member: Annan Chen, Tianqi Shen

UNIs: [ac4619, ts3255]









