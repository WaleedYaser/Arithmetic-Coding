#!/usr/bin/env python
# encoding: utf-8

__title__ = "Arithmatic Coding test"
__author__ = "Waleed Yaser (waleedyaser95@gmail.com)"
__version__ = "1.0"

"""
    Arithmatic Coding test
    ~~~~~~~~~~~~~~~~~~~~~~
    A test code for implementing Arithmatic coding class.
        
    require:
        *python 2.7
"""

from Arithmatic import ArithmaticCoding

symbols = []
probs = []

dataFile = file("test_data.txt")

# Extract data from the file
for line in dataFile:
    symbols.append(line.split(" ")[0])
    probs .append(float(line.split(" ")[1]))


# New object from the class
ArthCode = ArithmaticCoding(symbols, probs, "$")

code = ArthCode.Compress("CAEE$") #Compress
word = ArthCode.Decompress(code)  #Decompress

# Output results
print "Arithmatic Coding test:"
print "~~~~~~~~~~~~~~~~~~~~~~~"
print 'Compress "CAEE$"'
print "Result:", code
print "_______________________"
print
print "Decompress:", code
print "Result:", word
print
print "======================="


