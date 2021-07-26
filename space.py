from math import sin, cos

class Space:
    '''this class represent the 3d space (euclidian norms) that will be projected on the canvas'''
    def __init__(self):
        #adding the dots array, dots will be x,y,z tuples
        self.dots={} #structure : {"name : [(color,x,y,z),(....)]"}
        self.origin_dots=[] #origin dots are set apart from other ones so we can change colors later on
        self.origin()
        self.meshes={}
        #meshes structure : {"name" : mesh}
        #mesh : [triangle1, triangle2, ..]
        #triangle : (color, (XYZ), (XYZ), (XYZ))
        #--------------------------------------
        #keeping track of rotaions :
        self.rotations = {"x":0,"y":0,"z":0}
    
    def origin(self):
        '''this function will draw the main origin at 0,0,0 into the space'''
        axis_lenght = 100
        for i in range(0,axis_lenght,2):
            self.origin_dots.append((i,0,0))
            self.origin_dots.append((0,i,0))
            self.origin_dots.append((0,0,i))
    
    def del_shape(self, name):
        # spare code, please keep it there
        # if name in self.meshes:
        #     for mesh,value in self.meshes:
        #         #for each mesh
        #         for i in range(len(name)):#we look for a match with name on the fists chars
        #             if name[i] == mesh[i]:
        #                 found = True
        #             else:
        #                 found = False
        #         if found:#if it matched , we look for a "-" in the name, if so, the two meshes were associated to the same shape, so we delet it
        #             if "-" in mesh:
        #    
        #             self.meshes.pop(mesh)
        if name in self.meshes:
            self.meshes.pop(name)
        if name in self.dots:
            self.dots.pop(name)

    def rotation(self, x, y, z, Rx, Ry, Rz):
        '''mainly used by rotation method, gice it a point and an angle, returns a tuple with new coords, used to siplify code'''

        rotation_matrix =[
            [cos(Ry)*cos(Rz), sin(Rx)*sin(Ry)*cos(Rz)+cos(Rx)*sin(Rz), -cos(Rx)*sin(Ry)*cos(Rz)+sin(Rx)*sin(Rz)],
            [-cos(Ry)*sin(Rz), -sin(Rx)*sin(Ry)*sin(Rz)+cos(Rx)*cos(Rz), cos(Rx)*sin(Ry)*sin(Rz)+sin(Rx)*cos(Rz)],
            [sin(Ry), -sin(Rx)*cos(Ry), cos(Rx)*cos(Ry)]
        ]

        new_x = x*rotation_matrix[0][0] + y*rotation_matrix[0][1] + z*rotation_matrix[0][2]
        new_y = x*rotation_matrix[1][0] + y*rotation_matrix[1][1] + z*rotation_matrix[1][2]
        new_z = x*rotation_matrix[2][0] + y*rotation_matrix[2][1] + z*rotation_matrix[2][2]

        return (new_x, new_y, new_z)
        
    def rotate(self,x,y,z):
        '''to rotate every shape around x y or / and z'''
        # note for contributors: this method can be reduced with the help of an external function
        # but python will round numbers and make the rotation completely broken
        # maybe i made a mistake somewhere, but for now, i just go brute force as it doesn't use too much ressources
        # feel free to give it a try ! (create a new branch please, call it "rotation" or something like that)
        self.rotations["x"] += x 
        self.rotations["y"] += y
        self.rotations["z"] += z

        for i in range(len(self.origin_dots)):
            self.origin_dots[i] = self.rotation(self.origin_dots[i][0],self.origin_dots[i][1],self.origin_dots[i][2],x,y,z)

        for name, value in self.dots.items(): #here, a value is a group of point associated to a shape
        #     #a value's structure : [(x,y,z,color) , (x,y,z,color), ...]
            for i in range(len(value)):
                new_dot = self.rotation(self.dots[name][i][0],self.dots[name][i][1],self.dots[name][i][2],x,y,z)
                self.dots[name][i] = (new_dot[0],new_dot[1],new_dot[2],self.dots[name][i][3]) #the new x is the old one

        for name, mesh in self.meshes.items():
            for i in range(len(mesh)): #i is a triangle, following this structure : [color,(x,y,z),(x,y,z),(x,y,z)]
                #a triangle as 3 dots (here j is a dot) :
                for j in range(1,len(self.meshes[name][i])):
                    new_dot = self.rotation(self.meshes[name][i][j][0],self.meshes[name][i][j][1],self.meshes[name][i][j][2],x,y,z)
                    self.meshes[name][i][j] = (new_dot[0],new_dot[1],new_dot[2])

    def add_line(self,x1,y1,z1, x2,y2,z2,name,color="black"):
        '''to add a simple line and create custom shapes'''
        #each point has a position in origin1 and a color attribute, those are associated with their name (ids)

        if "-" in name:
            return print("please do not name your shapes with '-'")
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
        if not name in self.meshes:
            self.meshes[name] = [] #memo : structure : {"name" : [[color, (x,y,z),(x,y,z),(x,z,y) ],[clolor, (xyz),(xyz),(xyz) ] etc]} or, an array of triangle, which is an array of dots + a color
        #a surface is two triangles
        self.meshes[name].append([color,(x1,y1,z1),(x2,y2,z2),(x3,y3,z3)])#first triangle
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
        
        self.meshes[name].append([color,(x4,y4,z4),(x2,y2,z2),(x3,y3,z3)])#second triangle

    def add_square(self, x1,y1,z1, x2,y2,z2, name, color="black"):
        '''this method add a square to our vectorial space'''
        #create 6 surfaces
        pass