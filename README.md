# godfink
Jast a RPG game coding by python.

Language : python 3

> You need start [DB](https://github.com/rockerway/graphql-server) before start the game.

[Database (graphql-server)](https://github.com/rockerway/graphql-server)

> To avoid copyright issues, can't upload controversial files, u need to download some gif image and place in the `resources folder`

> `resources/mapObjects` (width = 100, height = 100). Image name corresponding from [grapyql-server/data/mapObjects.json](https://github.com/rockerway/graphql-server/blob/master/data/mapObjects.json)'s field `imageName`
>> bed.git
>
>> door.gif
>
>> home.gif
>
>> work1.gif
>
>> work2.git

> `resources/roles` (width < 100, height = 100). image name corresponding from [graphql-server/data/characters.json](https://github.com/rockerway/graphql-server/blob/master/data/characters.json)'s field `imageName`
>> player.gif
>
>> role1.gif
>
>> role2.gif
>
>> role3.gif
>
>> role4.gif
>
>> role5.gif
>
>> role6.gif
>
>> role7.gif

> `resources/shots` (width = config.ini>window>width,
> height = config.ini>window>height)
>> explosice.gif
>
>> fish.gif

## Install

run Go Lang container:

`docker build -f ./jail/DockerfileGO -t go:run ./jail`

run Python container:

`docker build -f ./jail/DockerfilePython -t python:run ./jail`

## Run Game

> You need start [DB](https://github.com/rockerway/graphql-server) before start the game

`python3 main.py`
