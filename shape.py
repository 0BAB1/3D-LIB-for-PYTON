# First of all, all shapes' meshes should look like this :
# [ triangle1, triangle2, etc.. ]
# and a triangle like this : 
# [shader, outline, (x,y,z), (x,y,z),(x,y,z)]
#
# shapes will be stored via references in a scene (or space) array, everytime a shape will use transform() method,
# scene shall update

class Shape:
    def __init__(self):
        pass