#!/usr/bin/python


import json
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)

exportdata = data

# trying to import a module, fails on run, will figure out later
#import mutagen

# input area, add input values here that will later end up in the json file. for now it will just be command line, later it will get a UI

title = input("Episode Title: ")
exportdata["title"] = title

subtitle = "<p>"
subtitle += input("Subtitle: ")
subtitle += "</p>"
exportdata["subtitle"] = subtitle


content = input("Episode description in HTML code: ")
exportdata["content"] = content

#trying to get length from mp3 but mutagen can't be loaded
"""
from mutagen.mp3 import MP3
audio = MP3("003_keynote.mp3")
print(audio.info.length)
"""

episode = input("Episode number (three digits): ")
exportdata["episode"] = episode

filename = input("Filename (Slug): ")
exportdata["filename"] = filename


humandate = input("Publication date (DD.MM.YYYY): ")
exportdata["humandate"] = humandate

with open('export.json', 'w') as outfile:
    json.dump(exportdata, outfile)
    
#testprint all data
pprint(exportdata)


