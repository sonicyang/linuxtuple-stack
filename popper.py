#!/usr/bin/env python

import time

import linuxtuples

conn = linuxtuples.connect()

while 1:
    index = int(conn.get(("stack", "sp", None))[2])
    if index == 0:
        conn.put(("stack", "sp", index))
        time.sleep(2)
        continue

    print("POP:", conn.get(("stack", index, None))[2])
    index = index - 1
    conn.put(("stack", "sp", index))

