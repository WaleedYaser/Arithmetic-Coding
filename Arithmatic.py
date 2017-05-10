
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

    def Decode(text, code, prob):

        range_low = {}
        range_high = {}

        p_low = 0
        for i in xrange(len(text)):
            range_low[text[i]] = p_low
            p_low += prob[i]
            range_high[text[i]] = p_low    
        
        low_old = 0
        high_old = 1
        _range = high_old - low_old
        
        terminator = '$'

        s = ""
        result = ""
        value = code
        
        while (s != terminator):
            for k, v in range_low.iteritems():
                if (value >= range_low[k] and value < range_high[k]):
                    print k, v, value, _range
                    result += k
                    low = range_low[k]
                    high = range_high[k]
                    _range = high - low
                    value = (value - low)/_range
                    if (k == terminator):
                        s = k
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
    
