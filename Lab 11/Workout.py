## Workout

import math

class vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.vec = [self.x, self.y, self.z]

    def __str__(self):
        return '['+str(self.x)+','+str(self.y)+','+str(self.z)+']'

    def vlist(self):
        return [self.x, self.y, self.z]

    def setValues(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __float__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        
    def __add__(lhand, rhand):
        return vec3(lhand.x + rhand.x, lhand.y + rhand.y, lhand.z + rhand.z)

    def __truediv__(lhand, rhand):
        return vec3(lhand.x / rhand, lhand.y / rhand, lhand.z / rhand)


x1, y1, z1 = input('Enter the first 3D vector values with space: ').split()
x2, y2, z2 = input('Enter the second 3D vector values with space: ').split()
mass = float(input('Enter a mass value: '))

vec1 = vec3(float(x1), float(y1), float(z1))
vec2 = vec3(float(x2), float(y2), float(z2))

totalvec = vec1 + vec2
acc = totalvec / mass

print(acc)
print(float(acc))

