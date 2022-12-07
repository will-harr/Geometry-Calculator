from tkinter import *
from shape_windows import *

class GUI:
    def __init__(self, window):
        self.window = window

        self.label1 = Label(window, text ='Select Shape')
        self.label1.pack(side='top', pady = 15)

        self.sel_shape = Frame(window)
        self.sel_shape.place(x = 30, y = 40)

        self.label2 = Label(self.sel_shape, text='2D shapes:')
        self.label2.pack()


        self.circle_button = Button(self.sel_shape, text = 'circle')
        self.circle_button.pack()
        self.circle_button.bind('<Button>', lambda e: circle_window(window))

        self.square_button = Button(self.sel_shape, text='square')
        self.square_button.pack()
        self.square_button.bind('<Button>', lambda e: square_window(window))

        self.rectangle_button = Button(self.sel_shape, text='rectangle')
        self.rectangle_button.pack()
        self.rectangle_button.bind('<Button>', lambda e: rectangle_window(window))

        self.triangle_button = Button(self.sel_shape, text='triangle')
        self.triangle_button.pack()
        self.triangle_button.bind('<Button>', lambda e: triangle_window(window))

        self.ellipse_button = Button(self.sel_shape, text='ellipse')
        self.ellipse_button.pack()
        self.ellipse_button.bind('<Button>', lambda e: ellipse_window(window))




        self.sel_3d = Frame(window)
        self.sel_3d.place(x=125, y=40)

        self.label3 = Label(self.sel_3d, text='3D shapes:')
        self.label3.pack()

        self.sphere_button = Button(self.sel_3d, text='sphere')
        self.sphere_button.pack()
        self.sphere_button.bind('<Button>', lambda e: sphere_window(window))

        self.cube_button = Button(self.sel_3d, text='cube')
        self.cube_button.pack()
        self.cube_button.bind('<Button>', lambda e: cube_window(window))

        self.ellipsoid_button = Button(self.sel_3d, text='ellipsoid')
        self.ellipsoid_button.pack()
        self.ellipsoid_button.bind('<Button>', lambda e: ellipsoid_window(window))

        self.cone_button = Button(self.sel_3d, text='cone')
        self.cone_button.pack()
        self.cone_button.bind('<Button>', lambda e: cone_window(window))






