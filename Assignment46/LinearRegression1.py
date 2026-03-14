import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def LinearReg():
    X = np.array([[1],[2],[3],[4],[5]])

    Y = np.array([50,55,60,65,70])

    Model = LinearRegression()

    Model.fit(X,Y)

    print("Cofficient :",Model.coef_)

    print("Intercept :",Model.intercept_)

    # Y = mX + C
    Y_Pred = 6
    Ans = Model.coef_ *Y_Pred + Model.intercept_

    print("Prediction for 6 study hours :",Ans)
    
def main():
    LinearReg()

if __name__ =="__main__":
    main()