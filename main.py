from tkinter import Grid
from shape import Line, Shape
from app import App
from space import Space
#FIRTS VERSION
#basic use : create a space and an application
space = Space()
application = App(space)

#create an origin
line1 = Line(0,0,0,100,0,0,"red","1")
line2 = Line(0,0,0,0,100,0,"red","2")
line3 = Line(0,0,0,0,0,100,"red","3")
space.add_shape(line1,0,0,0)
space.add_shape(line2,0,0,0)
space.add_shape(line3,0,0,0)

#test zone
lineTest = Line(0,0,0,150,150,200,"green","test")
space.add_shape(lineTest,20,40,60)

application.represent_space()
application.mainloop()