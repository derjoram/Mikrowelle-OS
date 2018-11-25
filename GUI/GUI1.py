#!/usr/bin/python

# trying to import a module, fails on run, will figure out later
#import mutagen

# input area, add input values here that will later end up in the json file. for now it will just be command line, later it will get a UI

title = input("Episode Title: ")

subtitle = "<p>"
subtitle += input("Subtitle: ")
subtitle += "</p>"

content = input("Episode description in HTML code: ")

#trying to get length from mp3 but mutagen can't be loaded
"""
from mutagen.mp3 import MP3
audio = MP3("003_keynote.mp3")
print(audio.info.length)
"""

episode = input("Episode number (three digits): ")

filename = input("Filename (Slug): ")

humandate = input("Publication date (DD.MM.YYYY): ")
"""{
		"chapters": [
		    {
		        "image": null,
		        "start": "00:22:46.190",
		        "title": "Chapter 1",
		        "url": "http://example.com/1/"
		    },
		    {
		        "image": null,
		        "start": "01:21:33.010",
		        "title": "Chapter 2",
		        "url": "http://example.com/2/"
		    },
		    {
		        "image": null,
		        "start": "01:17:00.130",
		        "title": "Chapter 3",
		        "url": "http://example.com/3/"
		    }
		],
		"content": "<p>Summary</p>",
		"date": "2013-06-09T22:55:48.500Z",
		"duration": "01:35:29.914",
		"episode": "001",
		"filename": "001",
		"humandate": "09.06.2013",
		"subtitle": "<p>It is just the beginning.</p>",
		"title": "001 Title"
	}"""