import tkinter as tk

class App (tk.Tk):
    def __init__(self, space):
        '''App main class, specify a 3d vectorial space'''
        #init window
        tk.Tk.__init__(self)
        self.geometry("720x480")
        self.resizable(False, False)
        #array containing dots on the screen
        self.dots = []
        self.meshes = []
        self.space = space
        #represent the space
        self.make_widgets()
        #binds
        self.m_canvas.bind_all("<Right>", lambda x: self.space.rotate(0,0.1,0), add="+")
        self.m_canvas.bind_all("<Right>", lambda x: self.represent_space(), add="+")
        self.m_canvas.bind_all("<Left>", lambda x: self.space.rotate(0,-0.1,0), add="+")
        self.m_canvas.bind_all("<Left>", lambda x: self.represent_space(), add="+")
        self.m_canvas.bind_all("<Down>", lambda x: self.space.rotate(-0.1,0,0))
        self.m_canvas.bind_all("<Down>", lambda x: self.represent_space(), add="+")
        self.m_canvas.bind_all("<Up>", lambda x: self.space.rotate(0.1,0,0))
        self.m_canvas.bind_all("<Up>", lambda x: self.represent_space(), add="+")
    
    def make_widgets(self):
        '''create a test canvas'''
        self.m_canvas = tk.Canvas(width=720, height=480, background="white")
        self.m_canvas.pack()

    def add_dot(self, x, y, color="black"):
        '''add dot a specified coords (x,y) on the canvas'''
        #create a black dot, create line returns its id so we can delete it later on
        self.dots.append(self.m_canvas.create_line(x+720/2, y+480/2, x+720/2+1, y+480/2, fill=color))
        #the 480 and 720 values are canvas' width and height, this has to be improved

    def reset(self):
        '''used to delete all dots on the screen'''
        for dot in self.dots:
            self.m_canvas.delete(dot)
        self.dots = []
        for mesh in self.meshes:
            self.m_canvas.delete(mesh)
        self.meshes = []

    def represent_space(self):
        '''this method wil add, one by one, all the space's dots with only their x and y coords (and refresh btw)'''
        self.reset() #get rid of dots in the canvas
            
        for dot in self.space.origin_dots:
            self.add_dot(dot[0], dot[1], "red")
        
        for name, mesh in self.space.meshes.items():
            #memo : structure : {"name" : [(color, (x,y,z),(x,y,z),(x,z,y) ),( (xyz),(xyz),(xyz) ) etc]} or, an array of mesh, which is a tuple of of dots + a color
            for triangle in mesh: 
                # mesh : [ (color,(dot1),(dot2),(dot3)) , (color,(dot1),(dot2),(dot3))]
                #  ^^list of triangles    ^^this is triangle 1     ^^ this is triangle 2    .. etc
                self.meshes.append(self.m_canvas.create_polygon(triangle[1][0]+720/2,triangle[1][1]+480/2,triangle[2][0]+720/2,triangle[2][1]+480/2,triangle[3][0]+720/2,triangle[3][1]+480/2,fill=triangle[0],outline="grey"))
                #and as always, only a projection so only x and y are taken, color last

        #structure of space.dots:
        #
        # {"name" : [(x,y,z,color) , (x,y,z,color) , ...] , ...}
        #
        # -- project dots on the canvas --

        for name, shape in self.space.dots.items():
            #as the dot is projected, only x and y coords wil be used
            for dot in shape:
                self.add_dot(dot[0], dot[1], dot[3])