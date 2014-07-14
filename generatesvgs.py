#!/bin/python

from tempfile import mkstemp
import fileinput
from shutil import move, copy
from os import remove, close, stat, mkdir
import csv

try:
    stat("output")
except:
    mkdir("output")

try:
    stat("output/svg")
except:
    mkdir("output/svg")

with open('names.csv', 'rb') as csvfile:
	names = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in names:
		filenamestring = row[1]+row[2]
		filenamestring = "".join(filenamestring.split())
		filenamestring = "output/svg/"+filenamestring+".svg"
		if row[0] == "ATTENDEE":
			copy("templates/attendee.svg",filenamestring)
		elif row[0] == "SPEAKER":
			copy("templates/speaker.svg",filenamestring)
		elif row[0] == "STAFF":
			copy("templates/speaker.svg",filenamestring)
		
		for line in fileinput.input(filenamestring, inplace=True):
			print line.replace("***firstname***", row[1])

		for line in fileinput.input(filenamestring, inplace=True):
			print line.replace("***lastname***", row[2])

		for line in fileinput.input(filenamestring, inplace=True):
			print line.replace("***twitter***", row[3])

		if len(row) > 4:
			for line in fileinput.input(filenamestring, inplace=True):
				print line.replace("***stuff1***", row[4])
		if len(row) > 5:
			for line in fileinput.input(filenamestring, inplace=True):
				print line.replace("***stuff2***", row[5])
		if len(row)> 6:
			for line in fileinput.input(filenamestring, inplace=True):
				print line.replace("***stuff3***", row[6])		

