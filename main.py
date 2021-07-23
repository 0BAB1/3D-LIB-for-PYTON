from app import App
from space import Space
#FIRTS VERSION
#basic use : create a space and an application
space = Space()
application = App(space)
space.add_line(0,0,0 ,50,0,0,"surf1","black")
space.add_surf(10,10,10,50,50,50,100,50,200,"surf1", "blue")
application.represent_space()
application.mainloop()