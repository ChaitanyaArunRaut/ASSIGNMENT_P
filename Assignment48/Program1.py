# Calculate the Mean of the dataset using numpy for following values.
# [6,7,8,9,10,11,12]

import numpy as np

Data = [6,7,8,9,10,11,12]
# Using numpy
Mean = np.average(Data)
print("Average of data is :",Mean)

# userDefine
Sum = 0
for i in Data:
    Sum = Sum + i

print("Sum of the data is :",Sum)

N = len(Data)
MeanX = Sum / N

print("Average of Data is :",MeanX)


