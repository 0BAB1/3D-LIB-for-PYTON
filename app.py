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
        self.triangles = []
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
        for triangle in self.triangles:
            self.m_canvas.delete(triangle)
        self.triangles = []

    def represent_space(self):
        '''this method wil add, one by one, all the space's dots with only their x and y coords (and refresh btw)'''
        self.reset() #get rid of dots in the canvas