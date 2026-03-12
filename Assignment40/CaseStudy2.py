from sklearn import tree
from sklearn.tree import DecisionTreeClassifier 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import plot_tree
from sklearn.metrics import(
    accuracy_score,
    ConfusionMatrixDisplay
)
import numpy as np
df = pd.read_csv("student_performance_ml.csv")
border = "-^-"*25
class CaseStudies  :
       
    def step1(self):
        #----------------------------------------------------------------
        print(border)
        print(df.head())
        print("Step 1 : Train the model with all the features")

        Feature_col = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
        self.x = df[Feature_col]
        self.y = df["FinalResult"]
        print(self.x.shape)
        print(self.y.shape)

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.x,self.y, test_size=0.2,random_state=42)
        self.Model1 = DecisionTreeClassifier(max_depth=2)

        self.Model1.fit(self.X_train,self.Y_train)

        self.Y_pred = self.Model1.predict(self.X_test)

        self.Accuracy = accuracy_score(self.Y_test,self.Y_pred)
        print("Accuracy of First model is :",self.Accuracy*100,"%")
        #----------------------------------------------------------------
    def Step_1(self):
        print(border)
        print("Step_1 : Use model.feature_importance to \n Disply important Score. ")
        importance = pd.DataFrame({
            "Feature": self.x.columns,
            "Importance": self.Model1.feature_importances_
        }).sort_values(by="Importance",ascending=False)

        print("Feature Importance :\n",importance)

    def Step2(self):
        print(border)
        print("Step 2 : Remove the column SleepHour from the Dataset")
        Feature_Col = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted"]
        x = df[Feature_Col]
        y = df["FinalResult"]

        print(x.shape)
        print(y.shape)

        X_train,X_test,Y_Train,Y_test = train_test_split(x,y,test_size=0.2,random_state=42)
        Model2 = DecisionTreeClassifier(max_depth=3)

        Model2.fit(X_train,Y_Train)
        Y_Pred = Model2.predict(X_test)

        Accuracy = accuracy_score(Y_test,Y_Pred)
        print("Accuracy of the second Model is :",Accuracy*100,"%")
        #----------------------------------------------------------------
    def Step3(self):
        print(border)
        print("Step 3 : Train model using only - StudyHours and Attendance")
        Feature_Col = ["StudyHours","Attendance"]
        x = df[Feature_Col]
        y = df["FinalResult"]

        print(x.shape)
        print(y.shape)

        x_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2,random_state=10)
        Model3 = DecisionTreeClassifier(max_depth=3)

        Model3.fit(x_train,Y_train)
        Y_pred = Model3.predict(X_test)
        Accuracy = accuracy_score(Y_test,Y_pred)
        print("Accuracy of the third Model is :",Accuracy*100,"%")
        #----------------------------------------------------------------
    def Step4(self):
        print(border)
        print("Step 4 : Create a DataFrame with 5 new student ")
        new_student = pd.DataFrame({
            "StudyHours" : [5,8,4,6,7],
            "Attendance" : [85,88,75,96,50],
            "PreviousScore" : [70,40,88,65,96],
            "AssignmentsCompleted" : [10,8,7,9,5],
            "SleepHours" : [7,8,6,5,7]
        })

        prediction = self.Model1.predict(new_student)
        for i, pred in enumerate(prediction):
            result = "Pass" if pred == 1 else "Fail"
            print(f"Student {i+1}: {result}")

        print("Prediction for new students :",prediction)
        #----------------------------------------------------------------
    def Step5(self):
        print(border)
        print("Step 5 : Calculate the accuracy score mannualy..")
        Correct = np.sum(self.Y_test == self.Y_pred)
        Mannual_accuracy = Correct / len(self.Y_test)

        print("\n Manual Accuracy :",Mannual_accuracy*100)
        print("sklearn Accuracy :",self.Accuracy*100)
        #----------------------------------------------------------------
    def Step6(self):
        print(border)
        print("Step6 :Identify Student where : Misclassified.")
        misclassified = self.X_test[self.Y_test != self.Y_pred]
        print("Misclassified students : \n",misclassified)
        print("Total Misclassified :",len(misclassified))
        #----------------------------------------------------------------
    def Step7(self):
        print(border)
        print("Step 7 : train model using random_state = 0, 10 ,42 each.")
        print("This step we perform in the 3rd step : Result gets change and also the accuracy of the model also gets change\n " \
        "When we change the random_state.  ")
        #----------------------------------------------------------------
    def Step8(self):
        print(border)
        print("Step 8 : Visualize the trained decision tree.\n" 
        "using from sklearn.tree import plot_tree")
        plt.figure(figsize=(10,12))
        plot_tree(self.Model1, feature_names=self.x.columns,class_names=["Fail","Pass"],filled=True)
        plt.title("Decision Tree Visualization")
        plt.show()
        #----------------------------------------------------------------
    def Step9(self):
        print(border)
        print("Step 9 : Creater a new column PerformaceIndex and train model and check the accuracy gets improved..")
        df["PerformanceIndex"] = (df["StudyHours"]*2) + df["Attendance"]
        self.x = df.drop("FinalResult",axis=1)
        self.y = df["FinalResult"]

        self.X_train,self.X_test,self.Y_train,self.Y_test = train_test_split(self.x,self.y,test_size=0.2,random_state=42)

        self.Model1 = DecisionTreeClassifier(random_state=42)
        self.Model1.fit(self.X_train,self.Y_train)

        self.Y_pred = self.Model1.predict(self.X_test)
        self.Accuracy = accuracy_score(self.Y_test,self.Y_pred)

        print("Accuracy after adding PerFormanceIndex :",self.Accuracy*100,"%")

    def Step10(self):
        print(border)
        print("Step 10 : Train model with max_depth = None")
        self.Model1 = DecisionTreeClassifier(max_depth=None,random_state=42)
        self.Model1.fit(self.X_train,self.Y_train)

        train_pred = self.Model1.predict(self.X_train)
        test_pred =  self.Model1.predict(self.X_test)  

        train_Accuracy = accuracy_score(self.Y_train,train_pred)
        test_Accuracy  = accuracy_score(self.Y_test,test_pred)      

        print("Training Accuracy if max_depth=None :",train_Accuracy*100,"%")
        print("Testing Accuracy when max_depth=None :",test_Accuracy*100,"%")
        

def main():
    CaseStudiesOBJ = CaseStudies()
    CaseStudiesOBJ.step1()
    CaseStudiesOBJ.Step_1()
    CaseStudiesOBJ.Step2()
    CaseStudiesOBJ.Step3()
    CaseStudiesOBJ.Step4()
    CaseStudiesOBJ.Step5()
    CaseStudiesOBJ.Step6()
    CaseStudiesOBJ.Step7()
    CaseStudiesOBJ.Step8()
    CaseStudiesOBJ.Step9()
    CaseStudiesOBJ.Step10()


if __name__ == "__main__":
    main()




