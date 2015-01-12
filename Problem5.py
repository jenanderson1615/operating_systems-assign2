#Jen Anderson
#anderjen@onid.oregonstate.edu
#CS311-400
#Homework2
#Problem1

import subprocess
import shlex

def who_sp():
	command = 'who'
	who = subprocess.Popen(command)

if __name__ == '__main__':
	who_sp()
