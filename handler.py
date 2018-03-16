#!/usr/bin/env python

import time
import os
import glob
import json

class Handler():
    """
        Initializes the Handler object. Sets the starting file index and the
        maximum number of individual data points to write to a file.
    """
    def __init__(self):
        self.last = None
        self.pointsWritten = 0
        self.pointsCeiling = 30 * 60 * 6
        self.fileIndex = "dataFiles/data_{}.txt".format(str(int(time.time())))


    """
        Appends the specified data point to the current data file.
    """
    def append(self, point=""):
        with open(self.fileIndex, "a") as f:
            self.pointsWritten += 1
            f.write(point + "\n")
            self.switchFiles()

    """
        Returns all data stored in the last 0 to 12 hour period.

        Static.
    """
    @staticmethod
    def all():
        files = glob.glob("dataFiles/*")
        multiple = len(files) > 1

        if multiple:
            current = max(files, key=os.path.getctime)
            files.remove(current)
            previous = max(files, key=os.path.getctime)
        else:
            current = files[0]

        l, c = [], []
        
        if multiple:
            with open(previous, "r") as f:
                for line in f.readlines():
                    l.append(json.loads(line))

        with open(current, "r") as f:
            for line in f.readlines():
                c.append(json.loads(line))

        return json.dumps(l + c)


    """
        Gets the latest data point, as recorded by the sensor.

        Static.
    """
    @staticmethod
    def latest():
        files = glob.glob("dataFiles/*")
        current = max(files, key=os.path.getctime)

        with open(current, "r") as f:
            return f.readlines()[-1].strip()

    
    """
        Updates the url of the current data file, resets the point counter, and
        saves the previous url.
    """
    def switchFiles(self):
        if self.pointsWritten >= self.pointsCeiling:
            self.pointsWritten = 0
            self.last = self.fileIndex
            self.fileIndex = "dataFiles/data_{}.txt".format(str(int(time.time())))


"""
This is testing.

h = Handler()

for i in range(0, 30 * 60 * 6 + 10):
    h.append(str(i))
    time.sleep(.001)

print Handler.all()
print Handler.latest()
"""
