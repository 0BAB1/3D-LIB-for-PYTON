class Shape:
    '''this class create a shape, with a transfomation tracker'''
    def __init__(self, name):
        self.name = name
        self.transformation = {
            "Tx" : 0,
            "Ty" : 0,
            "Tz" : 0,
            "Rx" : 0,
            "Ry" : 0,
            "Rz" : 0
        }
        self.position = (0,0,0) # the shape's postion relative to the main origin (middle of the screen)
        self.mesh = [] #an array of triangles : [triangle1 , triangle2 , etc...]
        #atriangle looks like this : [color, outline, (xyz),(xyz),(xyz)]

        
