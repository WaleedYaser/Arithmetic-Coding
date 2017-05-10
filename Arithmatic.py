#!/usr/bin/env python
# encoding: utf-8

__title__ = "Arithmatic Coding"
__author__ = "Waleed Yaser (waleedyaser95@gmail.com)"
__version__ = "1.0"

"""
    Arithmatic Coding
    ~~~~~~~~~~~~~~~~~
    A class for implementing Arithmatic coding.
    
    constructor takes 3 parameters:
        *symbols list
        *probalities list
        *terminator charachter

    There are 2 calable methods:
        *Compress: take the word to compress and return code.
        *Decompress: takes the compressed code and return word.
        
    require:
        *python 2.7
        *pyserial 2.7 library
"""

class ArithmaticCoding:
    """
        
    """
    def __init__(self, symbols, probs, terminator):
        """
            Construct the probability range table in
            dictionaries data type.
        """
        self.symbols = symbols
        self.probs = probs
        self.__InitRangeTable()
        self.terminator = terminator # End of word.
        
    def __InitRangeTable(self):
        """
            Complete the probability range table
            =============================================
            Symbol | Probability | Range low | Range high
            =============================================
                   |             |           |
            ============================================= 
        """
        self.rangeLow = {}
        self.rangeHigh = {}

        rangeStart = 0

        for i in xrange(len(self.symbols)):
            s = self.symbols[i]
            self.rangeLow[s] = rangeStart
            rangeStart += self.probs[i]
            self.rangeHigh[s] = rangeStart
        
    def Compress(self, word):   
        """
            Compress given word into Arimatic code and
            return code.
        """
        
        lowOld = 0.0
        highOld = 1.0
        _range = 1.0

        # Iterate through the word to find the final range.
        for c in word:
            low  = lowOld + _range * self.rangeLow[c]
            high = lowOld + _range * self.rangeHigh[c]
            _range = high - low

            # Updete old low & hihh
            lowOld = low
            highOld = high

        # Generating code word for encoder.
        code = ["0", "."] # Binary fractional number
        k = 2             # kth binary fraction bit

        value = self.__GetBinaryFractionValue("".join(code))
        while(value < low):
            # Assign 1 to the kth binary fraction bit
            code.append('1')
            value = self.__GetBinaryFractionValue("".join(code))
            if (value > high):
                # Replace the kth bit by 0
                code[k] = '0'
            value = self.__GetBinaryFractionValue("".join(code))
            k += 1

        return value

    def Decompress(self, code):
        """
            Uncompress given Arimatic code and return word.
        """
        s = "" # flag to stop the while loop
        result = ""
        while (s != self.terminator):
            # find the key which has low <= code and high > code
            for key, value in self.rangeLow.iteritems():
                if (code >= self.rangeLow[key] and code < self.rangeHigh[key]):
                    result += key # Append key to the result
                    # update low, high, code
                    low = self.rangeLow[key]
                    high = self.rangeHigh[key]
                    _range = high - low
                    code = (code - low)/_range
                    # chech for the terminator
                    if (key == self.terminator):
                        s = key
                        break
                    
        return result

    def __GetBinaryFractionValue(self, binaryFraction):
        """
            Compute the binary fraction value using the formula
            of:
                (2^-1) * 1st bit + (2^-2) * 2nd bit + ...
        """
        value = 0
        power = 1

        # Git the fraction bits after "."
        fraction = binaryFraction.split('.')[1]

        # Compute the formula value
        for i in fraction:
            value += ((2 ** (-power)) * int(i))
            power += 1

        return value
    
