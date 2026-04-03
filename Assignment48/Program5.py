# Calculate the TP,TN,FP,FN. for the following array.
# Actual = [1,1,1,1,0,0,0,0]
# Predicted = [1,1,0,1,0,1,0,0]

def Confussion_Metrix(Actual,Predicted):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for a, p in zip(Actual,Predicted):
        if a == 1 and p == 1:
            TP = TP + 1
        elif a == 0 and p == 0:
            TN = TN + 1
        elif a == 0 and p == 1:
            FP = FP + 1
        elif a == 1 and p == 0:
            FN = FN + 1

    return TP,TN,FP,FN

def main():
    Data = [1,1,1,1,0,0,0,0]
    Predicted = [1,1,0,1,0,1,0,0]

    TP,TN,FP,FN = Confussion_Metrix(Data, Predicted)

    print("Actual Positive and Predicted Positive(True Positive) :",TP)
    print("Actual Negative and Predicted Negative(True Negative) :",TN)
    print("Actual Negative and Predicted Positive(False Positive) :",FP)
    print("Actual Positive and Predicted Negative(False Negative) :",FN)

if __name__ =="__main__":
    main()