# Consider bellow Dataset 
# train linear regression model.
# plot regression line using matplotlib

import numpy as np
import matplotlib.pyplot as plt

def PredictSalary():
    border = "--^--"*20
    print(border)
    print("Step 1 : Load the Dataset :")
    print(border)

    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]

    print("Independent Variables are :",X)
    print("Dependent Variables are :",Y)
    #---------------------------------------------------------------------------------------------------
    print(border)
    print("Step 2 : Calculate the mean  :")
    print(border)
    n = len(X)

    mean_x = sum(X)/n
    mean_Y = sum(Y)/n

    print("mean of X :",mean_x,"\n Mean of y :",mean_Y)

    #---------------------------------------------------------------------------------------------------
    print(border)
    print("Step 3 : Calculate  slop  :")
    print(border)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_x)*(Y[i] - mean_Y)
        denominator = denominator + ((X[i] - mean_x)**2)

    m = numerator / denominator
    print("Slop(m) is :",m)

    #---------------------------------------------------------------------------------------------------
    print(border)
    print("Step 4 : Calculate Y intercept of line is C  :")
    print(border)

    C = mean_Y - (m * mean_x)
    print("Y intercept of linne is C :",C)

    #---------------------------------------------------------------------------------------------------
    print(border)
    print("Step 5 : Calculate Y (salary) prediction :")
    print(border)

    X_prediction = 6
    
    Y_predition = C + m*X_prediction
    print("Predicted salary of 6 years of experience is :",Y_predition)

    #---------------------------------------------------------------------------------------------------
    print(border)
    print("Step 6 : Plot regression line using matplotlib :")
    print(border)
    # Calculat regression line values 
    Y_line = []
    for i in range(n):
        Y_Val = m * X[i] + C
        Y_line.append(Y_Val)
    print("Regression line data",Y_line)

    # Scatter plot of actual data
    plt.scatter(X,Y, color = 'r',label = "Actual Data")

    # Regression Point 
    plt.plot(X,Y_line,color = 'g',label = "Regression Line")

    # Predicted Point 
    plt.scatter(X_prediction,Y_predition,color = 'blue',label = 'Predicted Salary')

    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.title("Salary Prediction using Linear Regression.") 

    plt.legend()
    plt.show()
def main():
    PredictSalary()

if __name__ == "__main__":
    main()

