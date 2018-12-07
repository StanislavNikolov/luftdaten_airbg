#!/bin/bash

curl 'http://archive.luftdaten.info/' | ./scripts/download/getAllHTMLSFromMain.sh | tail -n 30 | while read date; do
	mkdir data/$date
	curl "http://archive.luftdaten.info/$date" | ./scripts/download/getAllCSVsFromHTML.sh | parallel --will-cite -j 20 "[ -f data/$date/{} ] || wget \"http://archive.luftdaten.info/$date/{}\" -O \"data/$date/{}\""
done
