import math

def scal(v1,v2):
    '''takes two tuples and do u^v, return a tuple'''
    return(v1[1]*v2[2]-v1[2]*v2[1],v1[2]*v2[0]-v1[0]*v2[2],v1[0]*v2[1]-v1[1*v2[0]])

class Space:
    '''this class represent the 3d space (euclidian norms , p=2) that will be projected on the canvas'''
    def __init__(self):
        #adding the dots array, dots will be x,y,z tuples
        self.dots={}
        self.origin_dots=[] #origin dots are set apart from other ones so we can change colors later on
        self.origin()
        self.rotations = (0,0,0) #to keep track of all rotations for later-added shapes (x,y,z)
    
    def origin(self):
        '''this function will draw the main origin at 0,0,0 into the space'''
        axis_lenght = 100
        for i in range(0,axis_lenght,2):
            self.origin_dots.append((i,0,0))
            self.origin_dots.append((0,i,0))
            self.origin_dots.append((0,0,i))
    
    def del_shape(self, name):
        self.dots.pop(name)

    def rotate(self,x,y,z):
        '''to rotate every shapes around X0, Y0 and Z0 axis'''
        self.rotations = (self.rotations[0]+x,self.rotations[1]+y,self.rotations[2]+z)
        rotationY =[
            [math.cos(y),    0,    math.sin(y)],
            [0              ,1              ,0],
            [-math.sin(y),  0,     math.cos(y)]
        ]
        rotationX =[
            [1,           0,                  0],
            [0,     math.cos(x),   -math.sin(x)],
            [0,     math.sin(x),    math.cos(x)]
        ]
        rotationZ =[
            [math.cos(z),-math.sin(z),0],
            [math.sin(z),math.cos(z),0],
            [0,0,1]
        ]

        if not x==0:
            for name, value in self.dots.items(): #here, a value is a group of point associated to a shape
            #a value's structure : [(x,y,z,color) , (x,y,z,color), ...]
                for i in range(len(value)):
                    new_y=rotationX[1][0]*self.dots[name][i][0]+rotationX[1][1]*self.dots[name][i][1]+rotationX[1][2]*self.dots[name][i][2]
                    new_z=rotationX[2][0]*self.dots[name][i][0]+rotationX[2][1]*self.dots[name][i][1]+rotationX[2][2]*self.dots[name][i][2]

                    self.dots[name][i] = (self.dots[name][i][0], new_y, new_z, self.dots[name][i][3]) #the new x is the old one

            for i in range(len(self.origin_dots)):
                #   this line is optional as it is the rotation axis new_x=rotationX[0][0]*self.origin_dots[i][0]+rotationX[0][1]*self.origin_dots[i][1]+rotationX[0][2]*self.origin_dots[i][2]
                new_y=rotationX[1][0]*self.origin_dots[i][0]+rotationX[1][1]*self.origin_dots[i][1]+rotationX[1][2]*self.origin_dots[i][2]
                new_z=rotationX[2][0]*self.origin_dots[i][0]+rotationX[2][1]*self.origin_dots[i][1]+rotationX[2][2]*self.origin_dots[i][2]
                self.origin_dots[i] = (self.origin_dots[i][0], new_y, new_z) #the new x is the old one
        
        if not y==0:
            for name, value in self.dots.items(): #here, a value is a group of point associated to a shape
            #a value's structure : [(x,y,z,color) , (x,y,z,color), ...]
                for i in range(len(value)):
                    # we are doing a base change :
                    # syntax // <newcoord> = <matrixCoord>*<oldCoord> <-- repeat for x y and z
                    # NewX = 00*0(Old x) + 01*1(Old y) + 02*2(Old z)
                    # NewY = 10*0 + 11*1 + 12*2
                    # NewZ = 20*0 + 21*1 + 22*2
                    new_x=rotationY[0][0]*self.dots[name][i][0]+rotationY[0][1]*self.dots[name][i][1]+rotationY[0][2]*self.dots[name][i][2]
                    new_z=rotationY[2][0]*self.dots[name][i][0]+rotationY[2][1]*self.dots[name][i][1]+rotationY[2][2]*self.dots[name][i][2]
                    #apply new coords to dots
                    self.dots[name][i] = (new_x, self.dots[name][i][1], new_z, self.dots[name][i][3])
            
            #this time for origin dots (to improve btw)
            for i in range(len(self.origin_dots)):
                new_x=rotationY[0][0]*self.origin_dots[i][0]+rotationY[0][1]*self.origin_dots[i][1]+rotationY[0][2]*self.origin_dots[i][2]
                new_z=rotationY[2][0]*self.origin_dots[i][0]+rotationY[2][1]*self.origin_dots[i][1]+rotationY[2][2]*self.origin_dots[i][2]
                self.origin_dots[i] = (new_x, self.origin_dots[i][1], new_z)
        
        if not z==0:
            for name, value in self.dots.items(): #here, a value is a group of point associated to a shape
            #a value's structure : [(x,y,z,color) , (x,y,z,color), ...]
                for i in range(len(value)):
                    new_x=rotationZ[0][0]*self.dots[name][i][0]+rotationZ[0][1]*self.dots[name][i][1]+rotationZ[0][2]*self.dots[name][i][2]
                    new_y=rotationZ[1][0]*self.dots[name][i][0]+rotationZ[1][1]*self.dots[name][i][1]+rotationZ[1][2]*self.dots[name][i][2]

                    self.dots[name][i] = (new_x, new_y, self.dots[name][i][2], self.dots[name][i][3])
            
            for i in range(len(self.origin_dots)):
                new_x=rotationZ[0][0]*self.origin_dots[i][0]+rotationZ[0][1]*self.origin_dots[i][1]+rotationZ[0][2]*self.origin_dots[i][2]
                new_y=rotationZ[1][0]*self.origin_dots[i][0]+rotationZ[1][1]*self.origin_dots[i][1]+rotationZ[1][2]*self.origin_dots[i][2]
                self.origin_dots[i] = (new_x, new_y, self.origin_dots[i][2])

    def add_line(self,x1,y1,z1, x2,y2,z2,name,color="black"):
        '''to add a simple line and create custom shapes'''
        #each point has a position in origin1 and a color attribute, those are associated with their name (ids)
        self.dots[name] = []

        vector=[
            x2-x1,
            y2-y1,
            z2-z1
        ]

        for x in range(x1,x2):
            y=x*vector[1]/vector[0]
            z=x*vector[2]/vector[0]
            self.dots[name].append((x,y,z,color))
    
    def add_surf(self,x1,y1,z1,x2,y2,z2,x3,y3,z3,name,color="black"):
        '''to create surface give the orgin and final point, and the normal'''
        self.dots[name] = []

        AB = (x2-x1,y2-y1,z2-z1)
        AC = (x3-x1,y3-y1,z3-z1)


    def add_square(self, x1,y1,z1, x2,y2,z2, name, color="black"):
        '''this method add a square to our vectorial space'''
        # here on x axis , adding 1 dot/pixel, as it is a cube, 4 edeges go the same way, so we do it 4x, 
        # in Y=y1 / Z=z1 ,
        # then in Y=y2 / Z=z1,
        # then in Y=y1 / Z=z2
        # and finally on Y=y2 and Z=z2
        self.dots[name] = []
        for i in range(min(x1,x2), max(x1,x2)):
            #Y=y1 Z=1
            self.dots[name].append((i,y1,z1,color))
            #Y=y2 Z=z1
            self.dots[name].append((i,y2,z1,color))
            #Y=y1 Z=z2
            self.dots[name].append((i,y1,z2,color))
            #Y=y2 Z=z2
            self.dots[name].append((i,y2,z2,color))
        
        #we now proceed to do the same on Y and Z
        for i in range(min(y1,y2), max(y1,y2)):
            #X=x1 Z=z1
            self.dots[name].append((x1,i,z1,color))
            #X=x2 Z=z1
            self.dots[name].append((x2,i,z1,color))
            #X=x1 Z=z2
            self.dots[name].append((x1,i,z2,color))
            #X=x2 Z=z2
            self.dots[name].append((x2,i,z2,color))

        for i in range(min(z1,z2), max(z1,z2)):
            #X=x1 Y=y1
            self.dots[name].append((x1,y1,i,color))
            #X=x2 Y=y1
            self.dots[name].append((x2,y1,i,color))
            #X=x1 Y=y2
            self.dots[name].append((x1,y2,i,color))
            #X=x2 Y=y2
            self.dots[name].append((x2,y2,i,color))