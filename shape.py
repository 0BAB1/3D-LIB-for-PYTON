from typing import List
from rotation import rotation

class Shape:
    '''this class create a shape, with a transfomation tracker'''
    def __init__(self, id="none"):
        self.id = id
        self.position = (0,0,0) # the shape's postion relative to the main origin (middle of the screen)
        self.mesh = [] #an array of triangles : [triangle1 , triangle2 , etc...]
        #atriangle looks like this : [color, outline, (xyz),(xyz),(xyz)]

    def transform(self, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0):
        '''rotate and translate the shape'''
        if not rx == 0 or not ry == 0 or not rz == 0:
            for i in range(len(self.mesh)):
                for j in range(2, len(self.mesh[i])):
                    self.mesh[i][j] = rotation(self.mesh[i][j][0],self.mesh[i][j][1],self.mesh[i][j][2], rx, ry, rz)
        if not tx == 0 or not ty == 0 or not tz == 0 :
            self.position = (self.position[0] + tx, self.position[1]+ty, self.position[2]+tz)
                
    def set_position(self, x, y, z):
        self.position = (x,y,z)

class Line(Shape):
    '''line shape, give it tow dots to link'''
    def __init__(self, x1, y1, z1, x2, y2, z2, color = "black", id="none"):
        super().__init__(id)
        #append a single triangle with 3 allgned dots
        self.mesh.append(["",color,(x1,y1,z1), (x1,y1,z1), (x2,y2,z2)])