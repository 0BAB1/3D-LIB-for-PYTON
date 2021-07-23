# 3D FOR TKINTER

this python script will allow you to get basic 3d prewiews on a python canvas or your tkinter projects, there aree no dependencies to install, only tkinter and math !

# How to use it ?

## initialize your vizualisation window :

```python
from app import App
from space import Space

#create a 3d space where your shapes will evolve
space = Space()

#create an app and specify the space your want to show on the screen
application = App(space)

#this tkinter method will lunch the window's main loop
application.mainloop()
```

## add shapes with those commands (!! between space and mainloop !!):

```python
#add a line, with two dots
space.add_line(x1,y1,z1, x2,y2,z2, "name","color")

#add a surface, with three dots
space.add_surf(x1,y1,z1, x2,y2,z2, x3,y3,z3, "name", "color")

#you can also remove a shape
space.del_shape("name")
```

the project is new, more shapes and possibilities comming soon !

## see what you made

You can now see thing on your windows's canvas when you lunch the app !
This dotted lines is the main origin, it is not considered as a shape.
If you did evverything corectly, your shapes will show up the canvas, you will have to use arrow keys to move thing around.
