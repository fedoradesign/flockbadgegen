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

try:
    stat("output/svg/background")
except:
    mkdir("output/svg/background")

copy("templates/background/prague-garrett.jpg","output/svg/background/prague-garrett.jpg")

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
			copy("templates/staff.svg",filenamestring)

		if row[5] == "No":
			for line in fileinput.input(filenamestring, inplace=True):
				print line.replace('inkscape:label="#vegan"', 'inkscape:label="#vegan" style="display:none"')
			for line in fileinput.input(filenamestring, inplace=True):
				print line.replace('inkscape:label="#veg"', 'inkscape:label="#veg" style="display:none"')
		elif row[5] == "Vegan":
			for line in fileinput.input(filenamestring, inplace=True):
				print line.replace('inkscape:label="#veg"', 'inkscape:label="#veg" style="display:none"')
		for line in fileinput.input(filenamestring, inplace=True):
			print line.replace("***firstname***", row[1])

		for line in fileinput.input(filenamestring, inplace=True):
			print line.replace("***lastname***", row[2])

		for line in fileinput.input(filenamestring, inplace=True):
			if row[3] == "":
				print line.replace("***twitter***", row[3])
			else:
				print line.replace("***twitter***", "@"+row[3])

		for line in fileinput.input(filenamestring, inplace=True):
			print line.replace("***stuff1***", row[4])	

