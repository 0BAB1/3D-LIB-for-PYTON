from math import sin, cos
from shape import Shape
from typing import List
from rotation import rotation

class Space:
    '''this class represent the 3d space (euclidian norms) that will be projected on the canvas'''
    def __init__(self):
        self.shapes = List['Shape'] #list containig all the shape to render on the scene
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

    def add_shape(self, shape):
        '''add a shape to render'''
        self.shapes.append(shape)