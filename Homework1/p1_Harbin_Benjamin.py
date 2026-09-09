#import matplotlib.pyplot as plt
#import numpy as np
import math

def QuadraticEquation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("no real solutions\n")
    elif discriminant == 0:
        OneSolution(a,b)
    else:
        TwoSolutions(a, b, discriminant)

def OneSolution(a, b):
    print(f"one solution: { -b/(2*a)}\n")

def TwoSolutions(a, b, discriminant):
    x1 = (-b + math.sqrt(discriminant))/2*a
    x2 = (-b - math.sqrt(discriminant))/2*a
    print(f"two solutions: x1={x1} x2= {x2}\n")

def main():
    while True:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        QuadraticEquation(a,b,c)
        
        


if __name__ == '__main__':
    main()