#Jen Anderson
#anderjen@onid.oregonstate.edu
#CS311-400
#Homework2
#Problem3

import urllib2
import sys

#My command line arguments
myURL = sys.argv[1]
fileToWrite = sys.argv[2]
myURL = 'http://' + myURL

#Get the url source code into variable name urlSourceCode
file = urllib2.urlopen(myURL)
urlSourceCode = file.read()

#write the source code to fileToWrite
fileHandle = open(fileToWrite, 'w')
fileHandle.write(urlSourceCode)
fileHandle.close()
