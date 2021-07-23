import math

class Space:
    '''this class represent the 3d space (euclidian norms) that will be projected on the canvas'''
    def __init__(self):
        #adding the dots array, dots will be x,y,z tuples
        self.dots={} #structure : {"name : [(color,x,y,z),(....)]"}
        self.origin_dots=[] #origin dots are set apart from other ones so we can change colors later on
        self.origin()
        self.rotations = (0,0,0) #to keep track of all rotations for later-added shapes (x,y,z)
        self.meshes={} #structure : {"name" : [(color, (xyz),(xyz),(xzy) ),( (xyz),(xyz),(xyz) )]} or, an array of triangle, which is a tuple of of dots + a color
    
    def origin(self):
        '''this function will draw the main origin at 0,0,0 into the space'''
        axis_lenght = 100
        for i in range(0,axis_lenght,2):
            self.origin_dots.append((i,0,0))
            self.origin_dots.append((0,i,0))
            self.origin_dots.append((0,0,i))
    
    def del_shape(self, name):
        self.dots.pop(name)
        self.meshes.pop(name)

    def rotate(self,x,y,z):
        '''to rotate every shape around x y or / and z'''
        rotationX =[
            [1,0,0],
            [0,math.cos(x),-math.sin(x)],
            [0,math.sin(x),math.cos(x)]
        ]
        rotationY =[
            [math.cos(y),0,math.sin(y)],
            [0 ,1,0],
            [-math.sin(y),0,math.cos(y)]
        ]
        rotationZ =[
            [math.cos(z),-math.sin(z),0],
            [math.sin(z),math.cos(z),0],
            [0,0,1]
        ]

        for name, value in self.dots.items(): #here, a value is a group of point associated to a shape
        #a value's structure : [(x,y,z,color) , (x,y,z,color), ...]
            for i in range(len(value)):
                pass

        # for dot in self.origin_dots:
        #     dot = rotation(dot,x,y,z)

        for name, mesh in self.meshes.items():
            #rotation for triangles in mesh
            # memo : mesh : [ (color,(dot1),(dot2),(dot3)) , (color,(dot1),(dot2),(dot3))]
            #      ^^list of triangles    ^^this is triangle 1          ^^ this is triangle 2    .. etc
            for i in range(len(mesh)):
                pass
        
        #this time for origin dots (to improve btw)
        for i in range(len(self.origin_dots)):
            pass

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

    def add_surf(self, x1,y1,z1 ,x2,y2,z2 ,x3,y3,z3, name, color="black"):
        '''create a surface with 2 triangles , the first dot is the ORIGIN of your surface, the main diagonal wiil start from here'''
        self.meshes[name] = [] #memo : structure : {"name" : [(color, (x,y,z),(x,y,z),(x,z,y) ),( (xyz),(xyz),(xyz) ) etc]} or, an array of triangle, which is a tuple of of dots + a color
        #a surface is two triangles
        self.meshes[name].append((color,(x1,y1,z1),(x2,y2,z2),(x3,y3,z3)))#first triangle
        #we need to determine our dot2-dot3 middle, this will later be shrter but for comprehension issues ... well its like that
        middlex = min(x2,x3) + (max(x2,x3)-min(x2,x3))/2
        middley = min(y2,y3) + (max(y2,y3)-min(y2,y3))/2
        middlez = min(z2,z3) + (max(z2,z3)-min(z2,z3))/2
        if x1 < middlex:
            x4 = x1 + 2*(middlex-x1)
        elif x1 > middlex:
            x4 = x1 - 2*(middlex-x1)
        else : #if we want to create a line
            x4 = x1
        
        if y1 < middley:
            y4 = y1 + 2*(middley-y1)
        elif y1 > middlex:
            y4 = y1 - 2*(middley-y1)
        else : #if we want to create a line
            y4 = y1

        if z1 < middlez:
            z4 = z1 + 2*(middlez-z1)
        elif y1 > middlex:
            z4 = z1 - 2*(middlez-z1)
        else : #if we want to create a line
            z4 = z1
        
        self.meshes[name].append((color,(x4,y4,z4),(x2,y2,z2),(x3,y3,z3)))#second triangle

    def add_square(self, x1,y1,z1, x2,y2,z2, name, color="black"):
        '''this method add a square to our vectorial space'''
        #we have to re-think that
        pass