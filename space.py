import math

class Space:
    '''this class represent the 3d space that will be projected on the canvas'''
    def __init__(self):
        #adding the dots array, dots will be x,y,z tuples
        self.dots=[]
        self.origin_dots=[] #origin dots are set apart from other ones so we can change colors later on
        self.origin()
        self.rotations = {"x" : 0, "y" : 0, "z" : 0} #to keep track of all rotations for later-added shapes
    
    def origin(self):
        '''this function will draw the main origin at 0,0,0 into the space'''
        axis_lenght = 100
        for i in range(0,axis_lenght,2):
            self.origin_dots.append((i,0,0))
            self.origin_dots.append((0,i,0))
            self.origin_dots.append((0,0,i)) #identity matrix ! coincidence ? i think not !
    
    def rotateY(self, angle=1):
        '''this method will rotate all the dots around y0 axis with the help of rotation matrix'''
        #the matrix to enable rotation around Y
        rotationY =[
            [math.cos(angle),0,math.sin(angle)],
            [0              ,1              ,0],
            [-math.sin(angle),0,math.cos(angle)]
        ]
        for i in range(len(self.dots)):
            # we are doing a base change :
            # syntax // <newcoord> = <matrixCoord>*<oldCoord> <-- repeat for x y and z
            # NewX = 00*0(Old x) + 01*1(Old y) + 02*2(Old z)
            # NewY = 10*0 + 11*1 + 12*2
            # NewZ = 20*0 + 21*1 + 22*2
            new_x=rotationY[0][0]*self.dots[i][0]+rotationY[0][1]*self.dots[i][1]+rotationY[0][2]*self.dots[i][2]
            new_y=rotationY[1][0]*self.dots[i][0]+rotationY[1][1]*self.dots[i][1]+rotationY[1][2]*self.dots[i][2]
            new_z=rotationY[2][0]*self.dots[i][0]+rotationY[2][1]*self.dots[i][1]+rotationY[2][2]*self.dots[i][2]
            #apply new coords to dots
            self.dots[i] = (new_x, new_y, new_z)
        
        #this time for origin dots (to improve btw)
        for i in range(len(self.origin_dots)):
            new_x=rotationY[0][0]*self.origin_dots[i][0]+rotationY[0][1]*self.origin_dots[i][1]+rotationY[0][2]*self.origin_dots[i][2]
            new_y=rotationY[1][0]*self.origin_dots[i][0]+rotationY[1][1]*self.origin_dots[i][1]+rotationY[1][2]*self.origin_dots[i][2]
            new_z=rotationY[2][0]*self.origin_dots[i][0]+rotationY[2][1]*self.origin_dots[i][1]+rotationY[2][2]*self.origin_dots[i][2]
            self.origin_dots[i] = (new_x, new_y, new_z)

    def rotateX(self, angle=1):
        '''this method will rotate all the dots around x0 axis with the help of rotation matrix'''
        #the matrix to enable rotation around Y
        rotationX =[
            [1,           0,                  0],
            [0,math.cos(angle),-math.sin(angle)],
            [0,math.sin(angle),math.cos(angle)]
        ]
        for i in range(len(self.dots)):
            new_x=rotationX[0][0]*self.dots[i][0]+rotationX[0][1]*self.dots[i][1]+rotationX[0][2]*self.dots[i][2]
            new_y=rotationX[1][0]*self.dots[i][0]+rotationX[1][1]*self.dots[i][1]+rotationX[1][2]*self.dots[i][2]
            new_z=rotationX[2][0]*self.dots[i][0]+rotationX[2][1]*self.dots[i][1]+rotationX[2][2]*self.dots[i][2]
            self.dots[i] = (new_x, new_y, new_z)

        for i in range(len(self.origin_dots)):
            new_x=rotationX[0][0]*self.origin_dots[i][0]+rotationX[0][1]*self.origin_dots[i][1]+rotationX[0][2]*self.origin_dots[i][2]
            new_y=rotationX[1][0]*self.origin_dots[i][0]+rotationX[1][1]*self.origin_dots[i][1]+rotationX[1][2]*self.origin_dots[i][2]
            new_z=rotationX[2][0]*self.origin_dots[i][0]+rotationX[2][1]*self.origin_dots[i][1]+rotationX[2][2]*self.origin_dots[i][2]
            self.origin_dots[i] = (new_x, new_y, new_z)
    
    def rotateZ(self, angle=1):
        '''this method will rotate all the dots around x0 axis with the help of rotation matrix'''
        #the matrix to enable rotation around Y
        rotationZ =[
            [math.cos(angle),-math.sin(angle),0],
            [math.sin(angle),math.cos(angle),0],
            [0,0,1]
        ]
        for i in range(len(self.dots)):
            new_x=rotationZ[0][0]*self.dots[i][0]+rotationZ[0][1]*self.dots[i][1]+rotationZ[0][2]*self.dots[i][2]
            new_y=rotationZ[1][0]*self.dots[i][0]+rotationZ[1][1]*self.dots[i][1]+rotationZ[1][2]*self.dots[i][2]
            new_z=rotationZ[2][0]*self.dots[i][0]+rotationZ[2][1]*self.dots[i][1]+rotationZ[2][2]*self.dots[i][2]
            self.dots[i] = (new_x, new_y, new_z)
        
        for i in range(len(self.origin_dots)):
            new_x=rotationZ[0][0]*self.origin_dots[i][0]+rotationZ[0][1]*self.origin_dots[i][1]+rotationZ[0][2]*self.origin_dots[i][2]
            new_y=rotationZ[1][0]*self.origin_dots[i][0]+rotationZ[1][1]*self.origin_dots[i][1]+rotationZ[1][2]*self.origin_dots[i][2]
            new_z=rotationZ[2][0]*self.origin_dots[i][0]+rotationZ[2][1]*self.origin_dots[i][1]+rotationZ[2][2]*self.origin_dots[i][2]
            self.origin_dots[i] = (new_x, new_y, new_z)

    def add_line(self,x1,y1,z1, x2,y2,z2):
        '''to add a simple line and create custom shapes'''
        vector=[
            x2-x1,
            y2-y1,
            z2-z1
        ]

        for x in range(x1,x2):
            y=x*vector[1]/vector[0]
            z=x*vector[2]/vector[0]
            self.dots.append((x,y,z))
    
    def add_square(self, x1,y1,z1, x2,y2,z2):
        '''this method add a square to our vectorial space'''
        # here on x axis , adding 1 dot/pixel, as it is a cube, 4 edeges go the same way, so we do it 4x, 
        # in Y=y1 / Z=z1 ,
        # then in Y=y2 / Z=z1,
        # then in Y=y1 / Z=z2
        # and finally on Y=y2 and Z=z2
        for i in range(x1, x2):
            #Y=y1 Z=1
            self.dots.append((i,y1,z1))
            #Y=y2 Z=z1
            self.dots.append((i,y2,z1))
            #Y=y1 Z=z2
            self.dots.append((i,y1,z2))
            #Y=y2 Z=z2
            self.dots.append((i,y2,z2))
        
        #we now proceed to do the same on Y and Z
        for i in range(y1, y2):
            #X=x1 Z=z1
            self.dots.append((x1,i,z1))
            #X=x2 Z=z1
            self.dots.append((x2,i,z1))
            #X=x1 Z=z2
            self.dots.append((x1,i,z2))
            #X=x2 Z=z2
            self.dots.append((x2,i,z2))

        for i in range(z1, z2):
            #X=x1 Y=y1
            self.dots.append((x1,y1,i))
            #X=x2 Y=y1
            self.dots.append((x2,y1,i))
            #X=x1 Y=y2
            self.dots.append((x1,y2,i))
            #X=x2 Y=y2
            self.dots.append((x2,y2,i))