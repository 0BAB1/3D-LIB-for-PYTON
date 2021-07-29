from algebra import rotation

class Camera():
    '''this is the camera class, give it a space to observe'''
    def __init__(self,space):
        self.position = (0,0,0)
        self.rotations = (0,0,0)
        self.space = space
        self.triangles = [] #the triangle to render and draw on app.py
        self.focal_lenght = 100
        #reminder : 
        #an array of triangles : [triangle1 , triangle2 , etc...]
        #atriangle looks like this : [color, outline, (xyz),(xyz),(xyz)]
    
    def transform(self,tx,ty,tz,rx,ry,rz):
        '''this methode will make the camera move around, rotate around it own axis'''
        self.position = (self.position[0]+tx,self.position[1]+ty,self.position[2]+tz)
        self.rotations = (self.rotations[0]+rx,self.rotations[1]+ry,self.rotations[2]+rz)
    def pre_render(self):
        '''this method execute the pre-render, to give the right coordonates directly to the main render in app.py'''
        # here is my strategy , we go aroud all dots,
        # we express all dots relatiely to our camera position,
        # which we quiclky apply rotation matrix with our self.rotation angles, but in negative
        # then we apply thales on, depending on :
        # focal_lenght / ditacnce = Xwelookingfor / X = Ywelookingfor / Y
        # we re-store everything as triangles and it's done
        self.triangles = [] #reset our tiangles list
        for i in range(len(self.space.shapes)): # a shape
            for j in range(len(self.space.shapes[i].mesh)): # a triangle
                triangle = ["","",(0,0),(0,0),(0,0)] #3 dots but in 2D so only X and Y for each dot
                #reminder :
                #an array of triangles : [triangle1 , triangle2 , etc...]
                #a triangle looks like this : [color, outline, (xyz),(xyz),(xyz)]
                for k in range(2,len(self.space.shapes[i].mesh[j])):
                    relativeCoords = (
                        self.space.shapes[i].mesh[j][k][0]-self.position[0],
                        self.space.shapes[i].mesh[j][k][1]-self.position[1],
                        self.space.shapes[i].mesh[j][k][2]-self.position[2]
                    )#coords relative to camera
                    print(relativeCoords)

                    temp_dot = rotation(
                        relativeCoords[0],
                        relativeCoords[1],
                        relativeCoords[2],
                        -self.rotations[0],
                        -self.rotations[1],
                        -self.rotations[2]
                    )
                    #apply thales on each dot of each triangle
                    #based on this formula : 
                    dot = (
                        (self.focal_lenght*temp_dot[0])/temp_dot[2],
                        (self.focal_lenght*temp_dot[1])/temp_dot[2],
                    )

                    #append the dot to the triangles
                    triangle[k] = dot
                triangle[0] = self.space.shapes[i].mesh[j][0] #color
                triangle[1] = self.space.shapes[i].mesh[j][1] #outine
                self.triangles.append(triangle)
                print(self.triangles)