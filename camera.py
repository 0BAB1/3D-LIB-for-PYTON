class Camera():
    '''this is the camera class, give it a space to ob'''
    def __init__(self,space):
        self.position = (0,0,0)
        self.transformations = {
            "Tx":0,"Ty":0,"Tz":0,
            "Rx":0,"Ry":0,"Rz":0
        }
        self.space = space
        self.triangles = []
        #reminder : 
        #an array of triangles : [triangle1 , triangle2 , etc...]
        #atriangle looks like this : [color, outline, (xyz),(xyz),(xyz)]

    def pre_render(self):
        pass
