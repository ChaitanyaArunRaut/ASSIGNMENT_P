from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
import numpy as np



Border = "--*--"*20
print(Border)
# Step 1 import the dataset 
print("Step 1 :Load the Data set...")
print(Border)

df = pd.read_csv("student_performance_ml.csv.")
print(df.head())
############################################################################
print(Border)
print("Step 2 : Deside Independent and Dependent Variable :")
print(Border)

feature_col = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

x = df[feature_col]
y = df["FinalResult"]

print("X shape :",x.shape) #(30, 5)
print("Y shape :",y.shape) # (30,)
############################################################################
print(Border)
print("Step 3 : Create a model and train it using fit() :")
print(Border)

X_train, X_Test, Y_train, Y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)
print("Data Spliting activity done.")
############################################################################
print(Border)
print("Step 4 : Builde a model :")
print(Border)

print("We are going to use DecisionTreeClassifier")

Model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=None,
    random_state=42
)
print("Model gets succesfully created...\n",Model)
############################################################################
print(Border)
print("Step 5 : Train the model")
print(Border)

Model.fit(X_train,Y_train)
print("Model Trainning completed...")
############################################################################
print(Border)
print("Step 6 : Test the Model:")
print(Border)

Y_pred = Model.predict(X_Test)
print("Model testing / Evaluation complete...")

print(Y_pred.shape)

print("Expected Answer :")
print(Y_test)
print("Predicted Answer :\n")
print(Y_pred)
############################################################################
print(Border)
print("Step 7 : Check the accuracy :")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)*100
print(f"Accuracy score of model : {accuracy}%")

Testting_accuracy = Model.score(X_train,Y_train)
print("Testing Accuracy of model is :",Testting_accuracy*100)

Trainning_accuracy = Model.score(X_train,Y_train)
print("Training accuracy is :",Trainning_accuracy*100)
############################################################################
print(Border)
print("Step 8 : Generate confusion matrix  :")
print(Border)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion metrix :")
print(cm)

True_Positive = np.sum((Y_pred == 0)&(Y_test == 0))
True_Negative = np.sum((Y_pred == 1)&(Y_test == 1))

print("True Positive ",True_Positive)
print("True negative",True_Negative)

print("Classification Report ")
print(classification_report(Y_test,Y_pred))


new_data = pd.DataFrame([[7,86,68,8,9]], columns=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"])

Y_pred = Model.predict(new_data)
if(Y_pred == [1]):
    print("Pass")
else:
    print("Fail")

    