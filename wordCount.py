# @Author: Jehu Alejandro Nunez
# Date: 8/31/2020
# Course: CS4375 Theory of Operating Systems
# Instructors: Eric Freudenthal


import os  # check if file exists
import re  # for regular expression
import sys # command line arguments

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCountTest.py <input text file> <output file> <solution key file>")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]
#Dictionary to store words
words = {}

#make sure text files exist
if not os.path.exists(inputFname):
    print ("text file input %s doesn't exist! Exiting" % inputFname)
    exit()

with open(inputFname, 'r') as thisFile:
    for line in thisFile:
        line = line.strip()
        for word in re.split("[\"'\s\t.,-;:]", line):
            if word.lower() == "":
                continue
            if word.lower() in words:
                words[word.lower()] += 1
            else:
                words[word.lower()] = 1

# Writting file
file = open(outputFileName, "w+")



# Words are sorted in order
for word, index in sorted(words.items()):

    file.write(word + " " + str(index) + "\n")


file.close()
