#!/usr/bin/env python

from handler import Handler
import data

h = Handler()

while True:
    now = data.now()
    h.append(now)
