#!/usr/bin/env python3
# Simple script to send a single command to the parsing code

import sys
from skillitor.core.queryparser import QueryParser

qp = QueryParser()
qp.parse_command(sys.argv[1])
