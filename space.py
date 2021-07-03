class Space:
    '''this class represent the 3d space that will be projected on the canvas'''
    def __init__(self):
        #adding the dots array, dots will be x,y,z tuples
        self.dots=[]
        self.add_square(10,10,10,100,100,200)
    
    def add_square(self, x1,y1,z1, x2,y2,z2):
        '''this method add a square to our vectorial space'''
        # here on x axis , adding 1 dot/pixel, as it is a cube, 4 edeges go the same way, so we do it 4x, 
        # in Y=y1 / Z=z1 ,
        # then in Y=y2 / Z=z1,
        # then in Y=y1 / Z=z2
        # and finally on Y=y2 and Z=z2
        for i in range(x1, x2):
            #Y=y1 Z=1
            self.dots.append((i,y1,z1))
            #Y=y2 Z=z1
            self.dots.append((i,y2,z1))
            #Y=y1 Z=z2
            self.dots.append((i,y1,z2))
            #Y=y2 Z=z2
            self.dots.append((i,y2,z2))
        
        #we now proceed to do the same on Y and Z