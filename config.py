
import sys
sys.path.append("D:/overviewer-0.19.9/") # Replace this with your path to manualmarkers.py,
# so python can find it

from manualmarkers import *                         # import our markers

# all the usual config stuff goes here

worlds["MineZ"] = "D:/MineZ"

renders["normalrender"] = {
    "world": "MineZ",
    "title": "MineZ Map",
    "rendermode": "smooth_lighting",
    "dimension": "overworld",
    "northdirection": "upper-right",
    'manualpois': mymarkers,
}

outputdir = "D:/minezmap"