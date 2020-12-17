import math
def square(a):
    area = a*a
    print(f'Area is: {area}')
    perimeter = 4*a
    print(f'Perimeter is: {perimeter}')  
def rectangle(a,b):
    area = a*b
    print(f'Area is: {area}')
    perimeter = 2*(a+b)
    print(f'Perimeter is: {perimeter}')
def triangle(x,y,z,a,b):
    area = 0.5*(a*b)
    print(f'Area is: {area}')
    perimeter = x+y+z
    print(f'Perimeter is: {perimeter}')
def triangleWithoutHieghtGiven(x,y,z):
    s=(x+y+z)/2
    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
    print(f'Area is: {area}')
    perimeter = x+y+z
    print(f'Perimeter is: {perimeter}')
def parallelogram(x,y,z,w,a,b):
    area = a*b
    print(f'Area is: {area}')
    perimeter = x+y+z+w
    print(f'Perimeter is: {perimeter}')
def circle(a):
    area = round(math.pi*a*a,3)
    print(f'Area is: {area}')
    perimeter = round(2*math.pi*a,3)
    print(f'Perimeter is: {perimeter}')
def rhombus(a,b):
    area = a*b
    print(f'Area is: {area}')
    perimeter = 4*a
    print(f'Perimeter is: {perimeter}')
def trapezoid(x,y,z,w,a,q,b):
    area = 0.5*((a+q)*b)
    print(f'Area is: {area}')
    perimeter = x+y+z+w
    print(f'Perimeter is: {perimeter}')



if __name__ == "__main__":
    n = input("Enter shape: \n").upper()
    if n == "SQUARE":
        a = float(input("Enter Side: \n"))
        square(a)
    if n == "RECTANGLE":
        a = float(input("Enter Length: \n"))
        b = float(input("Enter Breadth: \n"))
        rectangle(a,b)
    if n == "TRIANGLE":
        x = float(input("Enter 1st co-ordinate: \n"))
        y = float(input("Enter 2nd co-ordinate: \n"))
        z = float(input("Enter 3rd co-ordinate: \n"))
        a = float(input("Enter Base: \n"))
        b = float(input("Enter Height: \n"))
        triangle(x,y,z,a,b)
    if n == "TRIANGLEWITHOUTHIEGHTGIVEN":
        x = float(input("Enter 1st co-ordinate: \n"))
        y = float(input("Enter 2nd co-ordinate: \n"))
        z = float(input("Enter 3rd co-ordinate: \n"))
        triangleWithoutHieghtGiven(x,y,z)
    if n == "PARALLELOGRAM":
        x = float(input("Enter Length of 1st side: \n"))
        y = float(input("Enter Length of 2nd side : \n"))
        z = float(input("Enter Length of 3rd side : \n"))
        w = float(input("Enter Length of 4th side : \n"))
        a = float(input("Enter Base: \n"))
        b = float(input("Enter Height: \n"))
        parallelogram(x,y,z,w,a,b)
    if n == "CIRCLE":
        a = float(input('Enter radius: \n'))
        circle(a)
    if n == "RHOMBUS":
        a = float(input("Enter Base: \n"))
        b = float(input("Enter Height: \n"))
        rhombus(a,b)
    if n == "TRAPEZOID":
        x = float(input("Enter Length of 1st side: \n"))
        y = float(input("Enter Length of 2nd side : \n"))
        z = float(input("Enter Length of 3rd side : \n"))
        w = float(input("Enter Length of 4th side : \n"))
        a = float(input("Enter Large Base Length : \n"))
        q = float(input("Enter Small Base Length : \n"))
        b = float(input("Enter Height: \n"))
        trapezoid(x,y,z,w,a,q,b)
