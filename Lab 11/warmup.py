## Warmup

class rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
    def __str__(self):
        if self.numerator == 0:
            return '0'
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator)+'/'+str(self.denominator)
