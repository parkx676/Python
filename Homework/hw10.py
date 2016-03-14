## Imperial Measurements
## Juhwan Park(3917664)

class ImpMeas:
    def __init__(self, astr = "0'0\""):
        self.astr = astr.strip()
        for i in self.astr:
            if i == " ":
                self.astr = self.astr.replace(i, "")
        if self.astr.count("'") == 0:
            self.astr = "0'" + self.astr
            for i in self.astr:
                if i == '"':
                    self.astr = self.astr.replace(i, '')
            self.astr = self.astr.split("'")
        elif self.astr.count('"') == 0:
            self.astr = self.astr + '0'
            self.astr = self.astr.split("'")
        else:
            for i in self.astr:
                if i == "'":
                    self.astr = self.astr.replace(i, ' ')
                if i == '"':
                    self.astr = self.astr.replace(i, '')
            self.astr = self.astr.split()
        self.feet = int(self.astr[0])
        self.inch = int(self.astr[1])
        while self.inch > 11:
            self.inch -= 12
            self.feet += 1
                
    def __str__(self):
        return str(self.feet)+"'"+str(self.inch)+'"'

    def __repr__(self):
        return self.__str__()

    def __add__(lhand, rhand):
        total_inch = lhand.inch + rhand.inch
        total_feet = lhand.feet + rhand.feet
        while total_inch > 11:
            total_inch -= 12
            total_feet += 1
        return ImpMeas(str(total_feet)+"'"+str(total_inch)+'"')

    def __sub__(lhand, rhand):
        if lhand.inch == 0:
            lhand.inch += 12
            lhand.feet -= 1
        if rhand.inch == 0:
            rhand.inch += 12
            rhand.feet -= 1
        total_inch = abs(lhand.inch - rhand.inch)
        total_feet = abs(lhand.feet - rhand.feet)
        return ImpMeas(str(total_feet)+"'"+str(total_inch)+'"')

    def __mul__(lhand, rhand):
        total_inch = lhand.inch * rhand
        total_feet = lhand.feet * rhand
        if total_inch > 11:
            total_inch -= 12
            total_feet += 1
        return ImpMeas(str(total_feet)+"'"+str(total_inch)+'"')

    def __truediv__(lhand, rhand):
        total_inch = lhand.inch + lhand.feet * 12
        return ImpMeas(str(total_inch//rhand)+'"')

    def __mod__(lhand, rhand):
        total_inch = lhand.inch + lhand.feet * 12
        return ImpMeas(str(total_inch%rhand)+'"')

    
