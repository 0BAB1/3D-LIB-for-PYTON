from algebra import rotation

class Camera():
    '''this is the camera class, give it a space to observe'''
    def __init__(self,space):
        self.position = (0,0,0)
        self.rotations = {
            "x":0,"y":0,"z":0
        }
        self.space = space
        self.triangles = []
        self.focal_lenght = 2
        #reminder : 
        #an array of triangles : [triangle1 , triangle2 , etc...]
        #atriangle looks like this : [color, outline, (xyz),(xyz),(xyz)]

    def pre_render(self):
        '''this method execute the pre-render, to give the right coordonates directly to the main render in app.py'''
        # here is my strategy , we go aroud all dots,
        # we express all dots relatiely to our camera position,
        # which we quiclky apply rotation matrix with our self.rotation angles, but in negative
        # then we apply thales on, depending on :
        # focal_lenght / ditacnce = Xwelookingfor / X = Ywelookingfor / Y
        # we re-store everything as triangles and it's done
        for i in range(len(self.space.shapes)): # a shape
            for j in range(len(self.space.shapes[i])): # a triangle
                pass