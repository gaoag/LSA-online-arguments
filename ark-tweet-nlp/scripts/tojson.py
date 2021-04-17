#!/usr/bin/env python
# Take the pretsv format and make it CoNLL-like ("supertsv", having tweet metadata headers)
import sys

for line in sys.stdin:
    print(line)
