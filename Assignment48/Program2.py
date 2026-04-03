# Calculate the Mean of the dataset using numpy for following values.
# [6,7,8,9,10,11,12]

import numpy as np
import math
def Average(Data):
    Average = sum(Data)/len(Data)
    print("Average of the Data is :",Average)

    SqurtDev(Average,Data)

def SqurtDev(Mean,Data):
    # Calculate the Square of Deviation
    Deviation = []
    for i in Data:
        result = np.abs(i - Mean)** 2
        Deviation.append(result)

    # Calculate the sum of the Square Deviation
    SqrDevSum = sum(Deviation)
    print("Sum of the Quare Deviation is : ",SqrDevSum)

    CalVariance(SqrDevSum,Data)

def CalVariance(SumSqrDev, Data):
    # Calculate the Variacne.
    Variance = SumSqrDev/len(Data)
    print("Variance of Data is :",Variance)

    StdDeviation(Variance)

def StdDeviation(Variance):
    # Calculate the Standard Deviation
    #root = math.sqrt(Variance)
    StDeviation = Variance ** 0.5
    #print(root)
    print("Standard Deviation is :",StDeviation)

def main():
    Data = [6,7,8,9,10,11,12]

    Average(Data)

if __name__ == "__main__":
    main()

    
    