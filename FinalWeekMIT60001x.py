import numpy as np
import pylab as plt
import os
import math
# Charles Truscott, Final Week of MIT 6.000.1 Massachusetts Institute of Technology
# Plotting, continues to 6.000.2x

def main():
    x_vals = []
    for x in range(0, 100 + 1, 1):
        x_vals.append(x)
    myLinear = []
    myQuadratic = []
    myExponential = []
    myLogarithmic = []
    for y in range(0, 30 + 1, 1):
        myLinear.append(2 * y + 10)
        myQuadratic.append(2 * y ** 2 + 4 * y + 16)
        myExponential.append(1.5 ** y)
    cost_of_Invega_in_America = 300
    cost_of_Invega_in_Australia = 189
    cost_of_Invega_in_Australia_Concession = 5.80
    pal_cost = []
    pal_concentration_mghrs = []
    for y in range(0, 100 + 1, 1):
        pal_cost.append(cost_of_Invega_in_Australia_Concession * 12 * y)
    hours_in_a_year = 365 * 24
    miligrams_of_paliperidone_an_hour = (9 / 24)
    for y in range(0, 100 + 1, 1):
        pal_concentration_mghrs.append(miligrams_of_paliperidone_an_hour * hours_in_a_year * y)
    plt.xlabel("Years of paliperidone taken")
    plt.ylabel(" Miligrams of paliperidone ingested ")
    plt.plot(x_vals, pal_concentration_mghrs)
#    plt.xlabel("Years of Paliperidone Taken")
 #   plt.ylabel("Cost in dollars on a Welfare Payment (PBS)")
 #   plt.plot(x_vals, pal_cost)
#        myLogarithmic.append(math.log(y, math.e))
#    plt.plot(x_vals, myLinear)
#    plt.show()
#    plt.plot(x_vals, myQuadratic)
#    plt.show()
#    plt.plot(x_vals, myExponential)
    plt.show()
if __name__ == "__main__":main()