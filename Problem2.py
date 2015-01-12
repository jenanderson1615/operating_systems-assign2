#Jen Anderson
#anderjen@onid.oregonstate.edu
#CS311-400
#Homework2
#Problem2

import os
import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], "t:c:", ["term=", "class="])
for o, a in opts:
	if o == "-t":
		termname = a
	elif o == "--term":
		termname = a
	elif o == "-c":
		classname = a
	elif o == "--class":
		classname = a
	else:
		print "unhandled option"

def mymkdir(path):
	os.makedirs(path)

try:
	mymkdir('/nfs/stak/students/a/anderjen/' + termname + '/' + classname + '/assignments')
except OSError as e:
	if e.errno == 17:
		print "That directory already exists"

try:
	mymkdir('/nfs/stak/students/a/anderjen/' + termname + '/' + classname + '/examples')
except OSError as e:
	if e.errno == 17:
		print "That directory already exists"

try:
	mymkdir('/nfs/stak/students/a/anderjen/' + termname + '/' + classname + '/exams')
except OSError as e:
	if e.errno == 17:
		print "That directory already exists"

try:
	mymkdir('/nfs/stak/students/a/anderjen/' + termname + '/' + classname + '/lecture_notes')
except OSError as e:
	if e.errno == 17:
		print "That directory already exists"

try:
	mymkdir('/nfs/stak/students/a/anderjen/' + termname + '/' + classname + '/submissions')
except OSError as e:
	if e.errno == 17:
		print "That directory already exists"

try:
	os.symlink('/usr/local/classes/eecs/' + termname + '/' + classname + '/src/README', '/usr/local/classes/eecs/' + termname + '/' + classname + '/README')
except OSError as e:
	if e.errno == 17:
		print "README already exists"

try:
	os.link('/usr/local/classes/eecs/' + termname + '/' + classname + '/src', 'src_class')
except OSError as e:
	if e.errno == 17:
		print src_class + " already exists."
