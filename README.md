# godfink
Jast a RPG game coding by python.

Language : python 3

> You need start [DB]() before start the game

[Database (graphql-server)](https://github.com/rockerway/graphql-server)

## Install

run Go Lang container:

`docker build -f ./jail/DockerfileGO -t go:run ./jail`

run Python container:

`docker build -f ./jail/DockerfilePython -t python:run ./jail`

## Run Game

> You need start [DB]() before start the game

`python3 main.py`
