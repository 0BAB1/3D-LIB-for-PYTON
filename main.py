from app import App
from space import Space
#FIRTS VERSION

#basic use : create a space and an application
space = Space()
#COMMANDS
#
#as it is the first version, you can only create a square : space.add_square(x1,y1,z1,x2,y2,z2) and rotate it around with space.rotateX(angle) space.rotateY(angle) or space.rotateZ(angle)
#NB : angle in rad

#some examples :
space.add_square(0,0,0,150,150,150,"square1", "green")
space.add_line(0,0,0,150,150,150,"line1","pink")
# space.rotateX(.5)
# space.rotateY(.5)
# to delete a shape:
# space.del_shape("square1")
application = App(space)
application.mainloop()