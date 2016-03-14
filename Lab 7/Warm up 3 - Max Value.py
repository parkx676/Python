## Maximum values out of list

def maxValue( vals ):
    if len(vals) == 1:
        return vals[0]
    else:
        if vals[0] > vals[-1]:
            return maxValue(vals[:-1])
        else:
            return maxValue(vals[1:])
            
