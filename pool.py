#!/usr/bin/env python

import sys
import re
import datetime
import math

#============================================================
# main

def main(argv):
	try:
		f = open(argv[0], 'r')
	except IOError:
		print 'File not found.'
		sys.exit(0)
	f = open(argv[0], 'r')
	# Read line
	for line in f:
		# Check input for validity
		if check_input(line):
			# Calculate area to paint
			Area = find_area()
			print "Area =", Area
			# Calculate time needed to paint
			PaintDays, PaintHours = find_painting_time(Area)
			# Calculate volume of pool to fill
			Volume = find_volume()
			# Calculate time needed to fill
			FillDays, FillHours = find_filling_time(Volume)
			# Calculate elapsed time needed
			find_end_time(PaintDays, PaintHours, FillDays, FillHours)

#============================================================
# check_input(line)
#  Returns True if valid input values, else False

def check_input(line):
	global Length
	global Width
	global Shallow
	global Deep
	global Label

	print line
	# Line: length width shallow deep string
	patt = re.compile(r'(\d+)\s(\d+)\s(\d+)\s(\d+)\s(.*)')
	m = patt.match(line)
	if m:
		Length = int(m.group(1))
		Width = int(m.group(2))
		Shallow = int(m.group(3))
		Deep = int(m.group(4))
		Label = m.group(5)
	else:
		print "Bad syntax"
		return(False)
	if Deep < Shallow:
		print "Deep < Shallow"
		return(False)
	if Length < Width:
		print "Length < Width"
		return(False)
	return(True)

#============================================================
# find_area()
#  Returns area to paint in square feet

def find_area():
	global Length
	global Width
	global Shallow
	global Deep
	global Rise

	print "Length = ", Length
	print "Width = ", Width
	print "Shallow = ", Shallow
	print "Deep = ", Deep
	
	Rise = math.sqrt((Deep - Shallow)**2 + Length**2)
	print "Rise = ", Rise
	ShortWall = Width * Shallow
	TallWall = Width * Deep
	ShallowWall = Length * Shallow
	DeepWall = Length * Deep
	Bottom = Rise * Width

	Area = round((ShortWall + TallWall + ShallowWall + DeepWall + Bottom), 2)
	return(Area)

#============================================================
# find_painting_time(Area)
#  Returns number of days and hours needed to paint pool

def find_painting_time(Area):

	Time = Area/200
	print "Painting time =", Time
	Days = math.floor(Time / 8)
	print "Days =", Days
	Hours = Time - (Days * 8)
	print "Hours =", Hours
	return(Days, Hours)

#============================================================
# find_volume()
#  Returns number of gallons needed to fill pool

def find_volume():
	global Length
	global Width
	global Shallow
	global Deep
	global Rise

	Top = Length * Width * (Shallow - 0.5)
	Bottom = (Rise * Width * (Deep - Shallow)) / 2
	Volume = round((Top + Bottom) * 7.48, 2)
	print "Volume =", Volume
	return(Volume)

#============================================================
# find_filling_time(Volume)
#  Returns number of days and hours needed to fill the pool

def find_filling_time(Volume):

	Days = 0
	Days = math.floor(Volume / 1200)
	print "Days =", Days
	Rem = Volume - (Days * 1200)
	if Rem > 800:
		Hours = round(4 + (Rem - 800) / 400, 2)
	else:
		Hours = round(Rem / 800, 2)
	print "Hours =", Hours
	return(Days, Hours)
	
#============================================================
# find_end_time(PaintDays, PaintHours, FillDays, FillHours)

def find_end_time(PaintDays, PaintHours, FillDays, FillHours):
	print "Time"


#============================================================
# Main

if __name__ == "__main__":
	main(sys.argv[1:]) 
