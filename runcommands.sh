#!/bin/bash

apt-get install luarocks

luarocks install luasocket

cd hotelReservation

docker-compose build

docker-compose up -d

make run
