from app import App
from space import Space
#FIRTS VERSION
#basic use : create a space and an application
space = Space()
application = App(space)
space.add_line(0,0,0 ,100,100,100,"line1","green")
space.add_surf(0,0,0,50,0,0,0,50,0,"surf1", "blue")
space.del_shape("line1")
application.represent_space()
application.mainloop()