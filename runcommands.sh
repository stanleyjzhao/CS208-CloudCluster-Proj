#!/bin/bash

apt-get install luarocks

luarocks install luasocket

docker-compose build

docker-compose up -d

make run
