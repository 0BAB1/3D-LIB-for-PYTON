from app import App
from space import Space
#FIRTS VERSION


#basic use : create a space and an application
space = Space()
#COMMANDS
#
#as it is the first version, you can only create a square : space.add_square(x1,y1,z1,x2,y2,z2) and rotate it around with space.rotateX(angle) space.rotateY(angle) or space.rotateZ(angle)
#NB : angle in rad

# EXAMPLE : 
# space.add_square(100,100,100,200,200,300)
# space.rotateX(.1)
# space.rotateY(.5)
application = App(space)
application.mainloop()