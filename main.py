from app import App
from scene import Scene
#FIRTS VERSION
#basic use : create a space and an application
space = Scene()
application = App(space)
space.add_line(0,0,0 ,100,100,100,"line1","green")
space.add_surf(0,0,0,50,0,0,100,0,0,"surf1", "blue")
application.represent_space()
application.mainloop()