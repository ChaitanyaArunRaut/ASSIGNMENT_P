import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def DataClassifier(DataPath):

    border = "-->"*30
    #-----------------------------------------------------------------------------------------------------------
    print(border)
    print("Step 1 : Load the dataset from csv :")
    print(border)

    df = pd.read_csv(DataPath)
    print(df.shape)
    print(df.head())

    #-----------------------------------------------------------------------------------------------------------
    print(border)
    print("Step 2 :Clean the Dataset by removing empty row:")
    print(border)

    df.dropna(inplace=True)
    print("Total Records :",df.shape[0])
    print("Total columns :",df.shape[1])
    #-----------------------------------------------------------------------------------------------------------
    print(border)
    print("Step 3 : Saperate Independent and Dependent variables:")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of Independent variable :",X.shape)
    print("Shape of the Dependent Variables :",Y.shape)
    #-----------------------------------------------------------------------------------------------------------
    print(border)
    print("Step 4 : Split the dataset for training and testing :")
    print(border)  

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=11)

    print("Information of Training and Testing Dataset :")
    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)
    print("Shape of Y_train :",Y_train.shape)
    print("Shape of Y_test :",Y_test.shape)

    #-----------------------------------------------------------------------------------------------------------
    print(border)
    print("Step 5 : Train and test the model :")
    print(border)   

    # model selection
    Model = DecisionTreeClassifier(criterion="gini",max_depth=3)
    Model.fit(X_train,Y_train)

    Y_pred = Model.predict(X_test)

    print("Expected Answer :")
    print(Y_test)

    print("Predicted Answer :")
    print(Y_pred)
    
    #-----------------------------------------------------------------------------------------------------------
    print(border)
    print("Step 6 : Claculate the accuracy of the Model :")
    print(border) 

    Accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is :",Accuracy*100,"%")

def main():

    DataClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()