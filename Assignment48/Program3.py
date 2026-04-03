# Using Standard Scaler to perform feature Scaling 
# Data  = [[2520000],[3040000],[3580000]]
# print scaled Dataset 

import numpy as np
import math
    
def Average(Data):
    flat_data = []
    for i in Data:
        flat_data.append(i[0])
    print("Original Data is :",flat_data)
   
    # Calculate the Average
    Mean = sum(flat_data)/len(flat_data)
    print("Mean of data is :",Mean)

    Std_Deviation(flat_data,Mean)

def Std_Deviation(fData,Mean):
    Deviation = []
    for i in fData:
        result = np.abs(i-Mean)**2
        Deviation.append(result)

    Variance = sum(Deviation) / len(fData)
    Std_Dev = Variance ** 0.5

    print("Standard Deviation of Data is :",Std_Dev)

    Std_Scalling(Mean,Std_Dev,fData)

def Std_Scalling(mean, std_dev,fData):
    Std_scaleVal = []
    for i in fData:
        result = np.abs(i-mean)/std_dev
        Std_scaleVal.append(result)

    print("Scaled Values of the Data is :",Std_scaleVal)
def main():
    Data = [[2520000],
            [3040000],
            [3580000]
            ]

    Average(Data)

if __name__ == "__main__":
    main()
    