#!/usr/bin/env python

import linuxtuples

conn = linuxtuples.connect()

for i in range(0, 10):
    index = int(conn.get(("stack", "sp", None))[2])
    index = index + 1
    print("PUSH:", chr(96 + index))
    conn.put(("stack", index, chr(96 + index)))
    conn.put(("stack", "sp", index))
