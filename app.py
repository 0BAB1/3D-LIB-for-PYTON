import tkinter as tk

class App (tk.Tk):
    def __init__(self, space):
        '''App main class, specify a 3d vectorial space'''
        #init window
        tk.Tk.__init__(self)
        #here goes window infos
        self.canvas_width, self.canvas_height = 720 , 480
        self.ofFset = {"x" : self.canvas_width/2, "y" : self.canvas_height/2}
        self.geometry("720x480")
        self.resizable(False, False)
        #....................
        self.make_widgets()
        self.space = space
        self.meshes = []
        #mouse tracker to create Dx and Dy to generate rotation from mouse mouvement
        self.sensitivity = 0.4 #mouse sens.
        self.x = 0
        self.y = 0
        #binds
        self.m_canvas.bind_all("<B1-Motion>", self.motion)
        self.m_canvas.bind_all("<Motion>", self.refresh_mouse_position)

    def refresh_mouse_position(self, event):
        self.x, self.y = event.x, event.y

    def motion(self, event):
        x, y = event.x , event.y
        #make delta
        Dx = self.x-x
        Dy = self.y-y
        #update new x and y in app
        self.x, self.y = x, y
        self.space.rotate(-self.sensitivity*Dy/100,self.sensitivity*Dx/100,0)
        self.represent_space()
    
    def make_widgets(self):
        '''create a test canvas'''
        self.m_canvas = tk.Canvas(width=self.canvas_width, height=self.canvas_height, background="white")
        self.m_canvas.pack()

    def reset(self):
        '''used to delete all dots on the screen'''
        for mesh in self.meshes:
            self.m_canvas.delete(mesh)
        self.meshes = []

    def represent_space(self):
        '''this method wil add, one by one, all the space's dots with only their x and y coords (and refresh btw)'''
        self.reset() #get rid of dots in the canvas
        
        for name, mesh in self.space.meshes.items():
            #memo : structure : {"name" : [(color, outline,(x,y,z),(x,y,z),(x,z,y) ),( (xyz),(xyz),(xyz) ) etc]} or, an array of mesh, which is a tuple of of dots + a color
            for triangle in mesh: 
                # mesh : [ (color,outline,(dot1),(dot2),(dot3)) , (color,(dot1),(dot2),(dot3))]
                #  ^^list of triangles    ^^this is triangle 1     ^^ this is triangle 2    .. etc
                self.meshes.append(self.m_canvas.create_polygon(
                    triangle[2][0]+self.ofFset["x"],triangle[2][1]+self.ofFset["y"],
                    triangle[3][0]+self.ofFset["x"],triangle[3][1]+self.ofFset["y"],
                    triangle[4][0]+self.ofFset["x"],triangle[4][1]+self.ofFset["y"],
                    fill=triangle[0],outline=triangle[1]))
                #and as always, only a projection so only x and y are taken, color last