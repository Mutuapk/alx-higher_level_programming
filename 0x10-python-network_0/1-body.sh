#!/bin/bash
# Script to display body of 200 responses
curl -Lsi "$1" | head -n 1 | grep "200" > /dev/null && curl -Ls "$1"
