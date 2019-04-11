# ODD - On Demand Dev

ODD is an experiment in setting up a completely self contained Python 
development environment that requires nothing more than Docker and 
docker-compose to be installed on the host machine.

## Getting started

1. Make sure you have docker and docker-compose installed (obvs...).
2. Open a terminal and change to the directory that _odd_ is checked out into.
3. Run `docker-compose up`

This should first build the dev container (yes it will take a while the first
time), and then run both a Postgres database and the dev environment itself.

You can access the dev environment on http://127.0.0.1:8443 once it is up and
running

Once you have the editor up and running you will need to install the Python
extension and pip install the `requirements.txt`. Once that is done you should 
be good to go!


## TODO

- Work out how to have the docker build add the Python extension ahead of time

