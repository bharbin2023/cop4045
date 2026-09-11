import matplotlib.pyplot as plt
import numpy as np
import math

def plot_function(fun_str, domain, ns):
    xs = np.linspace(domain[0], domain[1], ns)
    ys=[]
    print(f"{'x':<5} {'y':>5}")
    print("-"*15)
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
        print_coords(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(fun_str)
    plt.plot(xs, ys,"o", markersize = 2, linestyle = '-')
    plt.show()
    
def print_coords(x,y):
    print(f"{x:+.4f} {y:+.4f}")


def main():
    fun_str = input("Enter a function with variable x: ")
    ns = int(input("Enter number of samples: ")) 
    xmin = float(input("Enter xmin: "))
    xmax = float(input("Enter xmax: "))
    domain = (xmin,xmax)
    plot_function(fun_str, domain, ns)
if __name__ == "__main__":
    main()