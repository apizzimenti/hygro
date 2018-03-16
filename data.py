#!/usr/bin/env python

import Adafruit_DHT
import datetime
import json

def now():
    humidity, temp = Adafruit_DHT.read_retry(11, 4)
    ltime = datetime.datetime.now()
    data = {
        "humidity": str(int(humidity)) + "%",
        "temperature": str((1.8 * temp) + 32),
        "time": str(ltime)
    }

    return json.dumps(data) 

