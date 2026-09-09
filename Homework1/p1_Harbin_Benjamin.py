import matplotlib.pyplot as plt
import numpy as np
import math

def QuadraticEquation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("no real solutions\n")

    elif discriminant == 0:
       x = OneSolution(a,b)
       graphOneSolution(a, b, c, x)

    else:
        r1,r2 = TwoSolutions(a, b, discriminant)
        graphTwoSolutions(a, b, c, r1, r2)

def OneSolution(a, b):
    x = -b/(2*a)
    print(f"one solution: {x}\n")
    return x

def TwoSolutions(a, b, discriminant):
    x1 = (-b + math.sqrt(discriminant))/2*a
    x2 = (-b - math.sqrt(discriminant))/2*a
    print(f"two solutions: x1={x1} x2= {x2}\n")
    return x1,x2

def graphOneSolution(a, b, c, root):
    x = np.linspace(root - 5, 0 + root + 5, 150)
    y = a * x**2 + b * x + c

    plt.plot(x, y,"o", markersize = 2, linestyle = '-', linewidth = "1")
    plt.plot(root,0,"*")#stars represent the root
    plt.show()

def graphTwoSolutions(a, b, c, r1, r2):
    x = np.linspace(r2 - 5, r1 + 5, 150)
    y = a * x**2 + b * x + c

    plt.plot(x, y,"o", markersize = 2, linestyle = '-', linewidth = "1")
    plt.plot(r1,0,"*")
    plt.plot(r2,0,"*")
    plt.show()
    

def main():
    cont = 1
    while cont != 0:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        QuadraticEquation(a,b,c)
        
        


if __name__ == '__main__':
    main()