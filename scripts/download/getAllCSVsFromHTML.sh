#!/bin/bash

grep -o 'href="[[:print:]]*csv"' | cut -c 6- | tr -d '"'
