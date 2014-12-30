#!/usr/bin/python


# inFile will be either "drew murphy domain" or "murphy, drew domain"

import sys
import re

# list of name and emails entries
entries = []

# Format types:
# 0 - dmurphy@sd46
# 1 - d.murphy@sd46
# 2 - drewmurphy@sd46
# 3 - drew.murphy@sd46
# 4 - drewm@sd46
# 5 - drew.m@sd46

# 6 - mdrew@sd46
# 7 - m.drew@sd46
# 8 - murphydrew@sd46
# 9 - murphy.drew@sd46
# 10 - murphyd@sd46
# 11 - murphy.d@sd46
fmtType = 0

def main(argv):

	if len(argv) < 3:
		print "Please specify an input text file and a format type (0-11)"
		exit()

	inFilename = argv[1]
	global fmtType
	fmtType = int(argv[2])
	if fmtType < 0 or fmtType > 11:
		print "Please specify a non-negative format type less than 11"
		exit()

	outFilename = "emails.txt"

	inFile = open(inFilename, "r+")
	with open(inFilename) as file:
		contents = file.readlines()

	for inEntry in contents:
		# ignore any one letter lines
		if len(inEntry) < 2:
			continue
		swap = False
		# handle comma and swap
		for char in inEntry:
			if char is ',':
				inEntry = inEntry.replace(',', '')
				swap = True
				inEntry = switchNames(inEntry)
		createEntries(inEntry, swap)

	writeEntries(outFilename)

def switchNames(inEntry):
	#re.split('\s+',inEntry)
	inEntry = inEntry.split()
	#print "inEntry: %s"%inEntry
	firstName = inEntry[1]
	lastName = inEntry[0]
	domain = inEntry[2]
	entry = firstName + ' ' + lastName + ' '  + domain
	return entry


def createEntries(inEntry, swap):
	
	inEntry = inEntry.split()
	#print "inEntry: %s\n"%inEntry

	firstName = inEntry[0]
	firstName = firstName.lower()
	firstInit = firstName[0]
	#print "firstName: %s firstInit: %s\n"%(firstName,firstInit)

	lastName = inEntry[1]
	lastName = lastName.lower()
	lastInit = lastName[0]
	#print "lastName: %s lastInit: %s\n"%(lastName,lastInit)

	domain = inEntry[2]

	# Create entry header
	if swap:
		upperFirstName = inEntry[1]
		upperLastName = inEntry[0]
	else:
		upperFirstName = inEntry[0]
		upperLastName = inEntry[1]
	header = '\n' + '=======================\n' + upperFirstName + ' ' + upperLastName + '\n'

	# dmurphy@sd46
	if fmtType is 0:
		entry = firstInit + lastName + domain + '\n'
		entries.extend(entry)
	# d.murphy@sd46
	if fmtType is 1:
		entry = firstInit + '.' + lastName + domain + '\n'
		entries.extend(entry)
	# drewmurphy@sd46
	if fmtType is 2:
		entry = firstName + lastName + domain + '\n'
		entries.extend(entry)
	# drew.murphy@sd46
	if fmtType is 3:
		entry = firstName + '.' + lastName + domain + '\n'
		entries.extend(entry)
	# drewm@sd46
	if fmtType is 4:
		entry = firstName + lastInit + domain + '\n'
		entries.extend(entry)
	# drew.m@sd46
	if fmtType is 5:
		entry = firstName + '.' + lastInit + domain + '\n'
		entries.extend(entry)

	# mdrew@sd46
	if fmtType is 6:
		entry = lastInit + firstName + domain + '\n'
		entries.extend(entry)
	# m.drew@sd46
	if fmtType is 7:
		entry = lastInit + '.' + firstName + domain + '\n'
		entries.extend(entry)
	# murphydrew@sd46
	if fmtType is 8:
		entry = lastName + firstName + domain + '\n'
		entries.extend(entry)
	# murphy.drew@sd46
	if fmtType is 9:
		entry = lastName + '.' + firstName + domain + '\n'
		entries.extend(entry)
	# murphyd@sd46
	if fmtType is 10:
		entry = lastName + firstInit + domain + '\n'
		entries.extend(entry)
	# murphy.d@sd46
	if fmtType is 11:
		entry = lastName + '.' + firstInit +domain + '\n'
		entries.extend(entry)


def writeEntries(outFilename):
	outFile = open(outFilename, "w+")
	for entry in entries:
		outFile.write(entry)



if __name__ == "__main__":
	main(sys.argv)
