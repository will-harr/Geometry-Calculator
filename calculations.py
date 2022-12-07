import math as m

def area_circle(radius):
    area = radius * radius * m.pi
    return area

def perimeter_circle(radius):
    perimeter = 2 * radius * m.pi
    return perimeter

def area_square(length):
    area = length * length
    return area

def perimeter_square(length):
    perimeter = length * 4
    return perimeter

def area_rectangle(length, width):
    area = length * width
    return area

def perimeter_rectangle(length, width):
    perimeter = (2 * length) + (2 * width)
    return perimeter

def area_triangle(side1, side2, side3):
    p = perimeter_triangle(side1, side2, side3) / 2
    area = m.sqrt(p * (p-side1) * (p-side2) * (p-side3))
    return area

def perimeter_triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

def area_ellipse(a, b):
    area = m.pi * a * b
    return area

def perimeter_ellipse(a, b):
    h = ((a-b)**2) / ((a+b)**2)
    p = m.pi * (a+b) * ((1+3*h)/(10 + m.sqrt(4-3*h)))
    return p

def sa_sphere(radius):
    sa = 4 * m.pi * radius * radius
    return sa

def volume_sphere(radius):
    v = (4/3) * m.pi * radius**3
    return v

def sa_cube(length):
    sa = (length**2) * 6
    return sa

def volume_cube(length):
    v = length**3
    return v

def sa_rect_prisim(length, width, height):
    sa = (2 * length *width) + (2 * length * height) + (2 * width * height)
    return sa

def volume_rect_prisim(length, width, height):
    v = length * width * height
    return v

def sa_ellipsoid(a, b, c):
    p = 1.6075
    d = (a**p) * (b**p)
    e = (a**p) * (c**p)
    f = (b**p) * (c**p)
    sa = 4 * m.pi * (((d+e+f)/3)**(1/p))
    return sa

def volume_ellipsoid(a, b, c):
    v = (4/3) * m.pi * a * b * c
    return v

def sa_cone(radius, height):
    length = m.sqrt((height**2) + (radius**2))
    sa = m.pi * radius * (radius + height)
    return sa

def volume_cone(radius, height):
    v = m.pi * (radius**2) * (height/3)
    return v

