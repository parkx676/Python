## Stretch

class measure:
    def __init__(self, feet = 0, inch = 0):
        self.feet = feet
        self.inch = inch
        if self.inch == 0:
            self.inch = self.feet
            self.feet = 0
        while self.inch > 11:
            self.inch -= 12
            self.feet += 1
    
    def __str__(self):
        if self.feet == 0 and self.inch == 0:
            return '0"'
        elif self.feet == 0:
            return str(self.inch)+'"'
        elif self.inch == 0:
            return str(self.feet)+"'"
        else:
            return str(self.feet)+"'"+str(self.inch)+'"'

    def __add__(lhand, rhand):
        return measure(lhand.feet + rhand.feet, lhand.inch + rhand.inch)

    def __sub__(lhand, rhand):
        if lhand.inch - rhand.inch < 0:
            lhand.feet -= 1
            lhand.inch += 12
        return measure(lhand.feet - rhand.feet, lhand.inch - rhand.inch)
