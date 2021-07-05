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
        self.space = space
        #represent the space
        self.make_widgets()
        self.represent_space()
    
    def make_widgets(self):
        '''create a test canvas'''
        self.m_canvas = tk.Canvas(width=720, height=480, background="gray")
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

    def represent_space(self):
        '''this method wil add, one by one, all the space's dots with only their x and y coords (and refresh btw)'''
        self.reset()
        #structure of space.dots:
        #
        # {"name" : [(x,y,z,color) , (x,y,z,color) , ...] , ...}
        #
        for name, shape in self.space.dots.items():
            #as the dot is projected, only x and y coords wil be used
            for dot in shape:
                self.add_dot(dot[0], dot[1], dot[3])
            
        for dot in self.space.origin_dots:
            self.add_dot(dot[0], dot[1], "red")
