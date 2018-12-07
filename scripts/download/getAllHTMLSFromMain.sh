#!/bin/bash

grep -o 'href="[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/"' | cut -c 6- | tr -d '"'
