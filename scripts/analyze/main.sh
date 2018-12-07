#!/bin/bash

if [ -f localcsvs ]; then
	echo "localcsvs exists, not gonna generate a new one" >&2
else
	echo "generating localcsvs..." >&2
	./scripts/analyze/runAllFilesThroughLocalFilter.sh > localcsvs
fi

echo "parsing and plotting data..." >&2
./scripts/analyze/analyzeFromFileList.py < localcsvs
#shuf localcsvs | head -n 200 | ./scripts/analyze/analyzeFromFileList.py
