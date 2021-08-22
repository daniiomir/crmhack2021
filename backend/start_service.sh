#!/usr/bin/env sh

docker build -t crmhack .
docker run -p 55555:55555 --name crmhack_app crmhack