#!/bin/bash
# takes in URL, sends a request, displays size of the body of response
curl -s "$1" | wc -c
