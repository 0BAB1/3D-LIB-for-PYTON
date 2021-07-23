from app import App
from space import Space
#FIRTS VERSION
#basic use : create a space and an application
space = Space()
application = App(space)
space.add_line(0,0,0 ,50,0,0,"surf1","black")
application.mainloop()