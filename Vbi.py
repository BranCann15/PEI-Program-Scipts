# ECE:2410 
# Homework 2 Problem 2
# Table Values and Graph
import math
import matplotlib.pyplot as plt

"""
Question 2: Consider a uniformly-doped Si pn-junction with doping concentrations
ðð=5Ã1018 cmâ3 and ðð=1Ã1016 cmâ3. Calculate the built-in potential barrier ððð 
as a function of temperature for 200 Kâ¤ð<500 K in steps of 25 K. Organize your 
values in a table. Next, make a neat plot of ððð versus temperature. 
Be sure to label axes and provide a title for the plot.
"""

def main():
    # constants
    K = 86*10**(-6) 
    k = 0.000236
    e = math.e

    # doping concentrations
    Na = 5*(10**18)
    Nd = 1*(10**16)

    # other variables/constants speciifc to problem 
    B = 5.23*(10**15)
    Eg = 1.1
    x, y = [], []

    # calculates all points and prints them
    for T in range(200,500,25):
        Ni = B*(T**(3/2))*e**(-Eg/(2*K*T))
        Vbi = ((k*T)/e)*math.log((Na*Nd)/(Ni**2))
        print(f"Temperature (K): {T} -> Vbi = {Vbi} : Ni = {Ni}") 
        x.append(T)
        y.append(Vbi)


    # plotting the points
    plt.plot(x, y, color="red", marker="o")
    
    # labels
    plt.xlabel('Temperature')
    plt.ylabel('Vbi')
    plt.title('Vbi versus Temerpature')
    
    # function to show the plot
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
