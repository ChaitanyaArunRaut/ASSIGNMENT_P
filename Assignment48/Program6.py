# Generate Classification Report.
# Actual = [1,1,1,1,0,0,0,0]
# Predicted = [1,1,0,1,0,1,0,0]
from sklearn.metrics import classification_report
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

def Classification_report(TP,TN,FP,FN):

    print("Calculate the Accuracy.")
    Accuracy = (TP + TN) / (TP + TN + FP + FN)
    print("Overall Correctness of the Model(Accurcy) :\n",Accuracy)

    print("Claculate Precision.")
    Precision = TP / (TP + FP)
    print("How many of the predicted positives are actually Positive (Precision): \n",Precision)

    print("Calculate Recall (Sensitivity)")
    Recall = TP / (TP + FN)
    print("How many actual positives were correctly predicted (Recall) :\n",Recall)

    print("Calculate F1 Score.")
    F1_score = 2*(Precision * Recall)/(Precision + Recall)
    print("Harmonic means of precision and recall (F1 Score) :\n",F1_score)

def Class_Rep(Actual,Predicted): 
    print("Generate Classification Report using inbuild Library.")
    Report = classification_report(Actual,Predicted)
    print("Classification Report Using Inbuild Library : \n",Report)


def main():
    Data = [1,1,1,1,0,0,0,0]
    Predicted = [1,1,0,1,0,1,0,0]

    TP,TN,FP,FN = Confussion_Metrix(Data, Predicted)

    print("Actual Positive and Predicted Positive(True Positive) :",TP)
    print("Actual Negative and Predicted Negative(True Negative) :",TN)
    print("Actual Negative and Predicted Positive(False Positive) :",FP)
    print("Actual Positive and Predicted Negative(False Negative) :",FN)

    
    Classification_report(TP,TN,FP,FN)
    Class_Rep(Data,Predicted)


if __name__ =="__main__":
    main()