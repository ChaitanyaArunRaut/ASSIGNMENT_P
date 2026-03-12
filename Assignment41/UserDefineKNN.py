#-------------K-Nearest Neighbores algorithm.-----------------------
# algorithm implemented manually without using any machine learning library.
# - Calculate Euclidean Distance 
# - Sort Distance
# - Select K nearest neighbors 
# - Predict the class based on majority voting.

# Q2 - Explain why the prediction changes when K increase.
# Ans - Because, k represents the number of nearest data points to make prediction.
# if we get lage value of k the votes will change and prediction also gets change.

import math
def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans
def UserDefineKNN():
#--------------------------------------------------------------------------------------------------------
    border = "--//--"*20
    print("Step 1 : Create the Dataset :")
    print(border)

    data = [{'point':'A','X': 1,'Y': 2,'label':'Red'},
            {'point':'A','X': 2,'Y': 3,'label':'Red'},
            {'point':'A','X': 3,'Y': 1,'label':'Blue'},
            {'point':'A','X': 6,'Y': 5,'label':'Blue'}
            ]

    print(border)
    print("UserDefine KNN :")

    for i in data:
        print(i)    

    new_point = {'X':2, 'Y':2}

    print(border)
#--------------------------------------------------------------------------------------------------------
    print("Step 2 : Claculate Distance")

    for d in data:
        d['distance'] = EucDistance(d,new_point)

        for d in data:
            print(d)
#--------------------------------------------------------------------------------------------------------

    print(border)
    print("Step 3 : Sort by distance :")
    print(border)

    sorted_data = sorted(data,key=lambda d : d['distance'])

    print("Sorted Data by the Distance :")
    for d in sorted_data:
        print(d)
    print(border)
    
#--------------------------------------------------------------------------------------------------------
    print("Step 4 : Select k = 3 nearest neignbors.")
    K = 5
    k_nearest = sorted_data[:K]
#--------------------------------------------------------------------------------------------------------
    print(border)
    print("Step 5 : Majority Voting")
    red = sum(1 for i in k_nearest if i['label']=='Red')
    Blue = 0
    for i in k_nearest:
        if i['label'] == 'Blue':
            Blue = Blue + 1
    
    print(f"Red Votes = {red}, Blue Votes = {Blue}")
    if red > Blue:
        print("Predicted class is : Red")
    else:
        print("Predicted Class is : Blue")

def main():
    UserDefineKNN()
    


if __name__ == "__main__":
    main()