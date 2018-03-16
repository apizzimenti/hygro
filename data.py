#!/usr/bin/env python

import Adafruit_DHT
import time
import json

def now():
    humidity, temp = Adafruit_DHT.read_retry(11, 4)
    ltime = time.time()
    data = {
        "humidity": humidity,
        "temperature": temp,
        "time": int(ltime)
    }

    return json.dumps(data) 

