#!/bin/bash
# takes in URL, sends a request, displays size of the body of response
curl -sI "URL" | grep -i "Content-Length" | grep -Eo "[0-9]+"

