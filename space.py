from math import sin, cos
from rotation import rotation

class Space:
    '''this class represent the 3d space (euclidian norms) that will be projected on the canvas'''
    def __init__(self):
        self.shapes = [] #list containig all the shape to render on the scene
        #meshes structure : {"name" : mesh}
        #mesh : [triangle1, triangle2, ..]
        #triangle : (color, (XYZ), (XYZ), (XYZ))
        #--------------------------------------
        #keeping track of rotaions :
        self.rotations = {"x":0,"y":0,"z":0}
    
    def del_shape(self, shape):
        '''get rid of a shape'''
        self.shapes.pop(shape)
        
    def rotate(self,x,y,z):
        '''to rotate every shape around x y or / and z'''
        self.rotations["x"] += x 
        self.rotations["y"] += y
        self.rotations["z"] += z
        #reminder : 
        #an array of triangles : [triangle1 , triangle2 , etc...]
        #atriangle looks like this : [color, outline, (xyz),(xyz),(xyz)]
        for i in range(len(self.shapes)):
            self.shapes[i].position = rotation(self.shapes[i].position[0],self.shapes[i].position[1],self.shapes[i].position[2],x,y,z)
            for j in range(len(self.shapes[i].mesh)):
                for k in range(2,len(self.shapes[i].mesh[j])):
                    self.shapes[i].mesh[j][k] = rotation(self.shapes[i].mesh[j][k][0],self.shapes[i].mesh[j][k][1],self.shapes[i].mesh[j][k][2], x,y,z)

    def add_shape(self, shape, x, y, z):
        '''add a shape to render at x y z coords'''
        shape.set_position(x,y,z)
        self.shapes.append(shape)