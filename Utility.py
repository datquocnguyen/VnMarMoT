
# -*- coding: utf-8 -*-

import os
import sys
#os.chdir("../")
#sys.setrecursionlimit(100000)
#sys.path.append(os.path.abspath(""))
#os.chdir("./VnMarMot")

def getColumnFormat(inputFile, outputFile):
	writer = open(outputFile, "w")
	with open(inputFile) as f:
	    for line in f:
	        words = line.strip().split()
	        for word in words:
	        	if word in ["“", "”", "''"]:
	        		writer.write("\"\n")
	        	else:
	        		writer.write(word + "\n")
	        writer.write("\n")
	writer.close()
if __name__ == "__main__":
	getColumnFormat(sys.argv[1], sys.argv[2])