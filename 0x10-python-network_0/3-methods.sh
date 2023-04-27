#!/bin/bash
# shows acceptable.methods by the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
