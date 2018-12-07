#!/bin/bash

find data -mindepth 2 | ./scripts/analyze/isLocal.py
