import tkinter as tk
from tkinter.constants import S
from algebra import rotation

class App (tk.Tk):
    def __init__(self, camera):
        '''App main class, specify a 3d vectorial space'''
        #init window
        tk.Tk.__init__(self)
        #here goes window infos
        self.canvas_width, self.canvas_height = 1280 , 720
        self.ofFset = {"x" : self.canvas_width/2, "y" : self.canvas_height/2}
        self.geometry("1280x720")
        self.resizable(False, False)
        #....................
        self.make_widgets()
        self.camera = camera
        self.triangles = []
        #mouse tracker to create Dx and Dy to generate rotation from mouse mouvement
        self.sensitivity = 0.4 #mouse sens.
        self.x = 0
        self.y = 0
        #binds
        self.m_canvas.bind_all("<B1-Motion>", self.motion)
        self.m_canvas.bind_all("<Motion>", self.refresh_mouse_position)
        self.m_canvas.bind_all("<Key>", self.move_camera)

    def move_camera(self, event):
        '''this method will move the camera around'''
        key = event.char
        # we have to make the camera go forward, depending on its orientation
        # we have to fond the vector that direct our translation of the camera
        vect_dir_z = rotation(0,0,10,self.camera.rotations[0],self.camera.rotations[1],self.camera.rotations[2])
        vect_dir_x = rotation(10,0,0,self.camera.rotations[0],self.camera.rotations[1],self.camera.rotations[2])
        if key == "z":
            self.camera.transform(vect_dir_z[0],vect_dir_z[1],vect_dir_z[2],0,0,0)
        if key == "q":
            self.camera.transform(-vect_dir_x[0],-vect_dir_x[1],-vect_dir_x[2],0,0,0)
        if key == "s":
            self.camera.transform(-vect_dir_z[0],-vect_dir_z[1],-vect_dir_z[2],0,0,0)
        if key == "d":
            self.camera.transform(vect_dir_x[0],vect_dir_x[1],vect_dir_x[2],0,0,0)

        self.render()

    def refresh_mouse_position(self, event):
        self.x, self.y = event.x, event.y

    def motion(self, event):
        x, y = event.x , event.y
        #make delta
        Dx = self.x-x
        Dy = self.y-y
        #update new x and y in app
        self.x, self.y = x, y
        self.camera.transform(0,0,0,-self.sensitivity*Dy/100,self.sensitivity*Dx/100,0) #if the space behave strangely, it might come fomr here, play around with + and -
        self.render()
    
    def make_widgets(self):
        '''create a test canvas'''
        self.m_canvas = tk.Canvas(width=self.canvas_width, height=self.canvas_height, background="white")
        self.m_canvas.pack()

    def reset(self):
        '''used to delete all dots on the screen'''
        for triangle in self.triangles:
            self.m_canvas.delete(triangle)
        self.triangles = []

    def render(self):
        self.reset()
        #we will go aroun
        self.camera.pre_render() #do the camera pre_render
        for i in range(len(self.camera.triangles)):#a triangle
            self.triangles.append(self.m_canvas.create_polygon(
                self.camera.triangles[i][2][0] + self.ofFset["x"] ,self.camera.triangles[i][2][1] + self.ofFset["y"],
                self.camera.triangles[i][3][0] + self.ofFset["x"] ,self.camera.triangles[i][3][1] + self.ofFset["y"],
                self.camera.triangles[i][4][0] + self.ofFset["x"] ,self.camera.triangles[i][4][1] + self.ofFset["y"],
                fill= self.camera.triangles[i][0],outline=self.camera.triangles[i][1]
            ))