from tkinter import Grid
from shape import Line, Shape
from app import App
from space import Space
from camera import Camera
#FIRTS VERSION
#basic use : create a space and an application
#we can only add line for now
space = Space()
camera = Camera(space)
application = App(camera)

#create an origin
line1 = Line(0,0,0,100,0,0,"red","1")
line2 = Line(0,0,0,0,100,0,"red","2")
line3 = Line(0,0,0,0,0,100,"red","3")
space.add_shape(line1,0,0,0)
space.add_shape(line2,0,0,0)
space.add_shape(line3,0,0,0)

#test zone
lineTest = Line(0,0,0,50,50,50,"green","test")
space.add_shape(lineTest,0,0,0)

camera.transform(0,0,-500,0,0,0)
camera.pre_render()
application.render()
application.mainloop()