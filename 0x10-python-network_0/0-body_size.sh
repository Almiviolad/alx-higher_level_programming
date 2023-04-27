#!/bin/bash
# prints the size of curl response from url
curl -s $1 | wc -c
