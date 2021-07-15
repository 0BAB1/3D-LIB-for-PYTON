from app import App
from space import Space
#FIRTS VERSION
#basic use : create a space and an application
space = Space()
application = App(space)
space.add_square(-10,-10,-10,-100,-100,100,"square1", "green")
space.add_surf(0,0,10,100,100,0,0,1,"surf1", "yellow")
application.mainloop()