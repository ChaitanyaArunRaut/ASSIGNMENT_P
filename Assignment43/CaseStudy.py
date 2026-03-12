# We have to design Machine Learning application which uses classification technique.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def Operations(Datapath):
    border = "--"*30 

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    print(border)
    print("Step 1 : Load the dataset : ")
    print(border)

    df = pd.read_csv(Datapath)
    print("Data Loaded Successfully...")
    print(df.shape)
    print(df.describe())
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    print(border)
    print("Step 2 : Clean and Manipulate Data : ")
    print(border)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)
    print(df.shape)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    print(border)
    print("Step 3 : Train the dataset  ")
    print(border)

    # Split the dataset into X and Y

    X = df[["TV","radio","newspaper"]]
    Y = df['sales']

    print("Independent Variables are :",X.shape)
    print("Dependent variables are :",Y.shape)

    # Split the Data to training and Testing.

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.5,random_state=42)

    # Create and Train the Model.
    Model = LinearRegression()

    Model.fit(X_Train,Y_Train)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    print(border)
    print("Step 3 : Test  the Model  ")
    print(border)

    Y_Pred = Model.predict(X_Test)
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    print(border)
    print("Step 4 : Disply actual prediction and Model Prediction. ")
    print(border)

    print("Actual Predicted Data :")
    print(Y_Test)

    print("Model Predicted Data :")
    print(Y_Pred)
    
def main():
    Operations("Advertising.csv")

if __name__ =="__main__":
    main()