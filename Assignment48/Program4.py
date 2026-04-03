# Calculate the Euclidean Distance between two points. 
# compare before and after applying feature scalling. 
# Explain the Difference in result.
# Data = [(10,20),(20,30)]
# p1 = [(10.20)], P2 = [(20,30)]


import numpy as np
import math

Border = "--"*40  

def EuclideanDist1(Data):
    print(Border)
    print("Step 1 :Calculate Euclidean Distance Beafore Scaling")
    print(Border)
    print("Formula : Dist = ((x1 - x2)**2 + (Y1 - Y2)**2) ")

    print("Original Data is :",Data)

    P1 = Data[0]
    P2 = Data[1]
    print("Point of the Data :\n","P1",P1,"\nP2",P2)
    
    Dist = math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)
    print("Distance  Before Scaling is : ",Dist)

def scaled_Data(Data):
    print(Border)
    print("Step 2 : Calculate new Scaled Points.")
    print(Border)
    # Seprate X and y
    X_Value = []
    Y_Value = []
    for i in Data:
        X_Value.append(i[0])
        Y_Value.append(i[1])

    print(X_Value,Y_Value)

    # Calculate the Mean 
    MeanX = sum(X_Value)/len(X_Value)
    MeanY = sum(Y_Value)/len(Y_Value)

    # Calculate the Deviation
    DeviationX = []

    for x in X_Value:
        resultX = (x - MeanX)**2
        DeviationX.append(resultX)

    DeviationY = []
    for y in Y_Value:
        resultY = (y - MeanY)**2
        DeviationY.append(resultY)

    # Calculate the Variance
    varienceX  = sum(DeviationX)/len(X_Value)
    varienceY = sum(DeviationY)/len(Y_Value)

    # Calculate the Std. Deviation

    Std_Dev_X = varienceX**0.5
    Std_Dev_Y = varienceY**0.5

    print("Std Deviation :",Std_Dev_X,Std_Dev_Y)

    # Scalling the data 
    Scaled_Points = []

    for i in range(len(Data)):
        X_scaled = (X_Value[i] - MeanX) / Std_Dev_X
        Y_scaled = (Y_Value[i] - MeanY) / Std_Dev_Y
        Scaled_Points.append((X_scaled,Y_scaled))
   
    print("Scaled points :",Scaled_Points)

    EuclideanDist2(Scaled_Points)

def EuclideanDist2(Data):
    print(Border)
    print("Step 3 :Calculate Euclidean Distance after Scaling")
    print(Border)
    print("Formula : Dist = ((x1 - x2)**2 + (Y1 - Y2)**2) ")

    P1 = Data[0]
    P2 = Data[1]

    Dist = math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)
    print("Distance after Scaling is :",Dist)
    
def main():
    Data = [(10,20),(20,30)]
   
    EuclideanDist1(Data)
    scaled_Data(Data)

if __name__ == "__main__":
    main()
    