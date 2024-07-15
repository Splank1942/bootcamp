import math


def rectangle_area():
    return rec_area

def circle_area():
    return circle_rad

def triangle_area():
    return tri_area

def square_perimeter():
    return square_perim

def circle_details():
    print(f"The circumference of the circle is: ",circum_circle)
    print(f"the area of the circle is: ",area_circle)
    

def geometry():
    if square_perim > circum_circle:
        print("The square has a larger perimeter")
    else:
        print("The circle has a larger circumference.")
    
    if rec_area > area_circle:
        print("The square has a larger area")
    else:
        print("The circle has a larger area")
    

    
    


x = int(input("what is side one of the rectangle? "))
y = int(input("what is side two of the rectangle? "))

rec_area = x * y

print(f"The area of the rectangle is:",rectangle_area())



r = int(input("What is the Radius of the Circle? "))

circle_rad = (r**2) * math.pi

print(f" The radius of the circle is:",circle_area())

a = int(input("What is the first side of the triangle? "))
b = int(input("What is the second side of the triangle? "))


tri_area = (a*b)/2

print(f"The area of the traiangle is:",triangle_area())

s = int(input("What is the length of the side of the square? "))

square_perim = s * 4

print(f"The perimeter of the square is:",square_perimeter())

ra = int(input("what is the radius of the circle? "))

area_circle = (ra**2) * math.pi

circum_circle = 2 * math.pi * ra


print(circle_details())

print(geometry())