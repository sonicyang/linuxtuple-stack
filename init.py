#!/usr/bin/env python

import linuxtuples

conn = linuxtuples.connect()
conn.put(("stack", "sp", 0))
