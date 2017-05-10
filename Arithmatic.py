
def Encode(text, word, prob):

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
    
    for c in word:
        print low_old, high_old, range_low[c], range_high[c], _range
        low  = low_old + _range * range_low[c]
        high = low_old + _range * range_high[c]
        _range = high - low
        low_old = low
        high_old = high
        print low, high, range_low[c], range_high[c], _range
        print "=" * 10

    code = ["0", "."]
    k = 2

    while(GetValue("".join(code)) < low):
        code.append('1')
        if (GetValue("".join(code)) > high):
            code[k] = '0'
        k += 1

    return GetValue("".join(code))

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

def GetValue(code):
    value = 0
    power = 1
    for i in code.split('.')[1]:
        value += ((2 ** (-power)) * int(i))
        power += 1

    return value
    
