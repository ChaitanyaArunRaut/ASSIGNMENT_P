# Implement Simple Linear Regression mannualy without using ML Libray
# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]
# Calculate - Mean of X (x-bar),Mean of Y(y-bar), Slope(m), Intercept(c)
import numpy as np
def Data_Prediction():
    Border = ":-:-:"*20
    print(Border)
    print("Step 1 : Load the Dataset :")
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independet variables :",X)
    print("Values of Dependent Variables :",Y)

    #-----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 2 : Calculate the Mean(Average) and Slop (M)")
    print(Border)
    # calculate X bar.
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("mean of X :",mean_X,"\n Mean of y :",mean_Y)
    n = len(X)
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i]-mean_X)*(Y[i]-mean_Y))
        denominator = denominator + ((X[i]-mean_X)**2)

    M = numerator/denominator
    print("Slop of line M :",M) 

    #-----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 3 : Calculate Y Intercept of line is C ")
    print(Border)

    C = mean_Y -(M * mean_X)
    print("Y Intercept of line is C :",C)
#-----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 4 : Calculate Y prediction :")
    print(Border)

    YP = []
    for i in (X):
        res = M*i+C
        YP.append(res)

    for i in (YP):
        print(i)
    
#-----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 5 : Mean Squared Error(MSE)")
    print(Border)  
    
    result = 0
    for i in range(n):
        result += (Y[i] - YP[i])**2
        print(result)
    print(result) 

    MSE = result / n

    print("Mean Square Error(MSE) is :",MSE)


#-----------------------------------------------------------------------------------------------------
    print(Border)
    print("Step 6 : Calculate r2 :)")
    print(Border)  
    Ans = 0
    Sum = 0
    for i in YP:
        Ans = ((i - mean_Y)**2)
        Sum = Sum + Ans
    print("Sum of numinitor (yp - y bar)2",Sum)

    Res = 0
    for i in Y:
        Res += (i -mean_Y)**2
    print("Sum of Denomination (y - y bar)2 :",Res) 

    R2 = Sum / Res
    print("calculation of R2 is :",R2)
def main():
    Data_Prediction()

if __name__ == "__main__":
    main()