from app import App
from space import Space
#FIRTS VERSION
#basic use : create a space and an application
space = Space()
application = App(space)
space.add_square(0,0,0,100,100,150,"square1", "green")
application.mainloop()