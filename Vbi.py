# ECE:2410 
# Homework 2 Problem 2
# Table Values and Graph
import math
import matplotlib.pyplot as plt
 
def main():
    K = 86*10**(-6) 
    k = 0.000236
    e = math.e

    Na = 5*(10**18)
    Nd = 1*(10**16)

    B = 5.23*(10**15)
    Eg = 1.1
    x, y = [], []

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