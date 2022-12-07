from tkinter import *
from calculations import *

class circle_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('circle')
        self.geometry('300x150')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 10)
        self.f1.pack()
        self.label1 = Label(self.f1, text='enter radius:')
        self.label1.pack(side = 'left')
        self.radius_entry = Entry(self.f1)
        self.radius_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the input in radius_entry
            radius = float(self.radius_entry.get())

            # check that radius is nonnegative and raise value error with message if not
            if radius < 0:
                raise TypeError('number must be non-negative')

            area = area_circle(radius)
            perimeter = perimeter_circle(radius)
            self.result_label.config(text= f'area: {area:.2f} square units\ncircumference: {perimeter:.2f} units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.radius_entry.delete(0, END)

class square_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('square')
        self.geometry('300x150')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 10)
        self.f1.pack()
        self.label1 = Label(self.f1, text='enter length:')
        self.label1.pack(side = 'left')
        self.length_entry = Entry(self.f1)
        self.length_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the input in length_entry
            length = float(self.length_entry.get())

            # check that length is nonnegative and raise value error with message if not
            if length < 0:
                raise TypeError('number must be non-negative')

            area = area_square(length)
            perimeter = perimeter_square(length)
            self.result_label.config(text= f'area: {area:.2f} square units\nperimeter: {perimeter:.2f} units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.length_entry.delete(0, END)


class triangle_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('triangle')
        self.geometry('300x200')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 5)
        self.f1.pack()
        self.label1 = Label(self.f1, text='side 1:')
        self.label1.pack(side = 'left')
        self.side1_entry = Entry(self.f1)
        self.side1_entry.pack(side = 'left')

        self.f4 = Frame(self, pady = 5)
        self.f4.pack()
        self.label2 = Label(self.f4, text='side 2:')
        self.label2.pack(side = 'left')
        self.side2_entry = Entry(self.f4)
        self.side2_entry.pack(side = 'left')

        self.f5 = Frame(self, pady = 5)
        self.f5.pack()
        self.label3 = Label(self.f5, text='side 3:')
        self.label3.pack(side = 'left')
        self.side3_entry = Entry(self.f5)
        self.side3_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the inputs 
            side1 = float(self.side1_entry.get())
            side2 = float(self.side2_entry.get())
            side3 = float(self.side3_entry.get())

            # check that length is nonnegative and raise value error with message if not
            if (side1 < 0) or (side2 < 0) or (side3<0):
                raise TypeError('number must be non-negative')

            # check that the given triangle is possible
            if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
                raise TypeError('given triangle cannot exist')

            area = area_triangle(side1, side2, side3)
            perimeter = perimeter_triangle(side1, side2, side3)
            self.result_label.config(text= f'area: {area:.2f} square units\nperimeter: {perimeter:.2f} units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.side1_entry.delete(0, END)
        self.side2_entry.delete(0, END)
        self.side3_entry.delete(0, END)


class ellipse_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('ellipse')
        self.geometry('300x200')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 5)
        self.f1.pack()
        self.label1 = Label(self.f1, text='radius a:')
        self.label1.pack(side = 'left')
        self.a_entry = Entry(self.f1)
        self.a_entry.pack(side = 'left')

        self.f4 = Frame(self, pady = 5)
        self.f4.pack()
        self.label2 = Label(self.f4, text='radius b:')
        self.label2.pack(side = 'left')
        self.b_entry = Entry(self.f4)
        self.b_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the inputs
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())

            # check that length is nonnegative and raise value error with message if not
            if (a < 0) or (b < 0):
                raise TypeError('number must be non-negative')

            area = area_ellipse(a, b)
            perimeter = perimeter_ellipse(a, b)
            self.result_label.config(text= f'area: {area:.2f} square units\ncircumference: {perimeter:.2f} units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.a_entry.delete(0, END)
        self.b_entry.delete(0, END)


class rectangle_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('rectangle')
        self.geometry('300x200')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 5)
        self.f1.pack()
        self.label1 = Label(self.f1, text='length:')
        self.label1.pack(side = 'left')
        self.length_entry = Entry(self.f1)
        self.length_entry.pack(side = 'left')

        self.f4 = Frame(self, pady = 5)
        self.f4.pack()
        self.label2 = Label(self.f4, text='width:')
        self.label2.pack(side = 'left')
        self.width_entry = Entry(self.f4)
        self.width_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the inputs
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())

            # check that length is nonnegative and raise value error with message if not
            if (length < 0) or (width < 0):
                raise TypeError('number must be non-negative')

            area = area_rectangle(length, width)
            perimeter = perimeter_rectangle(length, width)
            self.result_label.config(text= f'area: {area:.2f} square units\nperimeter: {perimeter:.2f} units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.length_entry.delete(0, END)
        self.width_entry.delete(0, END)


class sphere_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('sphere')
        self.geometry('300x150')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 10)
        self.f1.pack()
        self.label1 = Label(self.f1, text='enter radius:')
        self.label1.pack(side = 'left')
        self.radius_entry = Entry(self.f1)
        self.radius_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the input in radius_entry
            radius = float(self.radius_entry.get())

            # check that radius is nonnegative and raise value error with message if not
            if radius < 0:
                raise TypeError('number must be non-negative')

            surface_area = sa_sphere(radius)
            volume = volume_sphere(radius)
            self.result_label.config(text= f'surface area: {surface_area:.2f} square units\nvolume: {volume:.2f} cubic units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.radius_entry.delete(0, END)


class cube_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('cube')
        self.geometry('300x150')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 10)
        self.f1.pack()
        self.label1 = Label(self.f1, text='enter length:')
        self.label1.pack(side = 'left')
        self.length_entry = Entry(self.f1)
        self.length_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the input in radius_entry
            length = float(self.length_entry.get())

            # check that radius is nonnegative and raise value error with message if not
            if length < 0:
                raise TypeError('number must be non-negative')

            surface_area = sa_cube(length)
            volume = volume_cube(length)
            self.result_label.config(text= f'surface area: {surface_area:.2f} square units\nvolume: {volume:.2f} cubic units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.length_entry.delete(0, END)


class ellipsoid_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('ellipsoid')
        self.geometry('300x200')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 5)
        self.f1.pack()
        self.label1 = Label(self.f1, text='radius a:')
        self.label1.pack(side = 'left')
        self.a_entry = Entry(self.f1)
        self.a_entry.pack(side = 'left')

        self.f4 = Frame(self, pady = 5)
        self.f4.pack()
        self.label2 = Label(self.f4, text='radius b:')
        self.label2.pack(side = 'left')
        self.b_entry = Entry(self.f4)
        self.b_entry.pack(side = 'left')

        self.f5 = Frame(self, pady = 5)
        self.f5.pack()
        self.label3 = Label(self.f5, text='radius c:')
        self.label3.pack(side = 'left')
        self.c_entry = Entry(self.f5)
        self.c_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the inputs
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            # check that length is nonnegative and raise value error with message if not
            if (a < 0) or (b < 0) or (c<0):
                raise TypeError('number must be non-negative')

            surface_area = sa_ellipsoid(a, b, c)
            volume = volume_ellipsoid(a, b, c)
            self.result_label.config(text= f'surface area: {surface_area:.2f} square units\nvolume: {volume:.2f} cubic units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.a_entry.delete(0, END)
        self.b_entry.delete(0, END)
        self.c_entry.delete(0, END)

class cone_window(Toplevel):
    def __init__(self, master = None):
        super().__init__(master=master)
        self.title('cone')
        self.geometry('300x200')
        self.resizable(False, True)

        self.f1 = Frame(self, pady = 5)
        self.f1.pack()
        self.label1 = Label(self.f1, text='radius:')
        self.label1.pack(side = 'left')
        self.radius_entry = Entry(self.f1)
        self.radius_entry.pack(side = 'left')

        self.f4 = Frame(self, pady = 5)
        self.f4.pack()
        self.label2 = Label(self.f4, text='height:')
        self.label2.pack(side = 'left')
        self.height_entry = Entry(self.f4)
        self.height_entry.pack(side = 'left')

        self.f2 = Frame(self)
        self.f2.pack()
        self.btn_calculate = Button(self.f2, text='calculate', command=self.calculate)
        self.btn_calculate.pack(side = 'left')
        self.btn_clear = Button(self.f2, text='clear', command=self.clear)
        self.btn_clear.pack(side='left')

        self.f3 = Frame(self)
        self.f3.pack()
        self.result_label = Label(self.f3)
        self.result_label.pack()

    def calculate(self):
        try:
            # retreive the inputs
            radius = float(self.radius_entry.get())
            height = float(self.height_entry.get())


            # check that length is nonnegative and raise value error with message if not
            if (radius < 0) or (height < 0):
                raise TypeError('number must be non-negative')

            surface_area = sa_cone(radius, height)
            volume = volume_cone(radius, height)
            self.result_label.config(text= f'surface area: {surface_area:.2f} square units\nvolume: {volume:.2f} cubic units')

        except TypeError as e:
            self.result_label.config(text=f'{e}')
        except:
            self.result_label.config(text='Error: enter a number')

    def clear(self):
        self.result_label.config(text='')
        self.radius_entry.delete(0, END)
        self.height_entry.delete(0, END)
