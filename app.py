import tkinter as tk

class App (tk.Tk):
    def __init__(self):
        '''App test class, init and .mainloop to run app'''
        #init window
        tk.Tk.__init__(self)
        self.geometry("720x480")
        self.resizable(False, False)
        self.make_widgets()
        #array containing dots on the screen
        self.dots = []
    
    def make_widgets(self):
        '''create a test canvas'''
        self.m_canvas = tk.Canvas(width=720, height=480, background="gray")
        self.m_canvas.pack()

    def reset(self):
        '''used to delete all dots on the screen'''
        for dot in self.dots:
            self.m_canvas.delete(dot)
        self.dots = []