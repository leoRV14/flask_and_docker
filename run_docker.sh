#!/bin/bash
docker build -t flask8888 .
docker run -d -p 8888:8888 --name flask_container flask8888
