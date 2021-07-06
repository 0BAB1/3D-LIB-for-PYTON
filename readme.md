# 3D FOR TKINTER

this python script will allow you to get basic 3d prewiews on a python canvas or your tkinter projects, there aree no dependencies to install, only tkinter and math !

# How to use it ?

it's simple to use, you first have to import space and app:

from space import Space
from app import App

create a space : space = Space()
create an application (wich is a windows that contains a canvas) and give it the space you want to represent : application = App(space)

then you can use basic commands to add shapes, and rotate things around :
-space.add_line(args)
-space.add_square(args)
-space.rotate(args)
-space.del_shape(args)

when you are happy with your shapes, represent the space with app.represent_space()

and keep the app alive with app.mainloop()