#!/usr/bin/env python3
# Pass in a quoted string on the command line to test the parsing code

import sys
from skillitor.core.queryparser import QueryParser

qp = QueryParser()
qp.parse_command(sys.argv[1])
