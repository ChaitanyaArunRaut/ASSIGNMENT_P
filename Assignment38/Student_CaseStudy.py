import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay   
)

Border = "-"*100
###################################################################################################
# Step 1 : Load the Dataset
###################################################################################################
print(Border)
print("Step : 1")
print(Border)

DatasetPath = "student_performance_ml.csv."

df = pd.read_csv(DatasetPath)
print("Initial entries from dataset ")
print(df.head())

print(Border)
print("Last 5 records of the dataset :")
print(df.tail())

print(Border)
# total number of data type in the data
print("Total number of Data types :\n",df.dtypes)

print(Border)
print("Step : 2")
print(Border)

# total number of student in the Dataset 
totalstd  = df.shape[0]
print("Total number of student in the dataset is :",totalstd)

print(Border)

# total pass student count 
Pass_Count = df["FinalResult"].value_counts().get(1,0)
print("Total number of passed student :",Pass_Count)

print(Border)

# Total fail student count
Fail_Count = df["FinalResult"].value_counts().get(0,0)
print("Total failed student is :",Fail_Count)

print(Border)
print("Step : 3")
print(Border,"\n")

# Using pandas function, calculate and display 
# Average studay of Hours

total_SHour = sum(df["StudyHours"])
print("Average Study hours is :",total_SHour /totalstd)
print("Average Attendence of student is :",sum(df["Attendance"])/totalstd)
print("Maximum Previous Score is :",max(df["PreviousScore"]))
print("Minimum Sleep hours of student is :",min(df["SleepHours"]))

print(Border)
print("Step : 4")
print(Border,"\n")

result_Distribution = df["FinalResult"].value_counts()
print("Result Distribution :\n")
print(result_Distribution)

print("Percentage of pass Student is :",(Pass_Count/df.shape[0])*100)
print("Persentage of fail student is :",(Fail_Count/df.shape[0])*100)

print(Border)
print("Step : 5")
print(Border,"\n")


print("If the previous numbers is > 55 \n"
      "and \n Attendence of student is more than the 75% \n"
      "and \n Study_hours is >=5. \n Then the chance of student get pass is increases... ")

print(Border)
print("Step : 6")
print(Border,"\n")

# histogram of study hours 

plt.figure(figsize=(7,5))
plt.hist(df["SleepHours"], color = "r", edgecolor = 'g')
plt.title("Sleeping Hours Histogram Diagram")
plt.xlabel("Sleeping Hours")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

print("Based on the Histogram :\n"
      "9 Students are sleeping 8 hours\n"
      "16 Student get sleep of 6-7 hours\n"
      "Remaining 5 students get a sleep of 5 hours\n")

print(Border)
print("Step : 7")
print(Border,"\n")
print("This Step contains the scaaterplot...")
# Draw scatter plot of Study Hours ve PreviousScore
plt.figure(figsize=(7,6))

sns.scatterplot(data= df,
                x = "StudyHours",
                y = "PreviousScore",
                hue = "FinalResult",
                palette={1: "green", 0 : "red"})

plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(8,6))
Pass_Student = df[df["FinalResult"]==1]
Fail_Student = df[df["FinalResult"]==0]

sns.scatterplot(x = Pass_Student["StudyHours"],
                y= Pass_Student["PreviousScore"],
                color = 'g',
                label = "Pass")

sns.scatterplot(x = Fail_Student["StudyHours"],
                y = Pass_Student["PreviousScore"],
                color = 'r',
                label = "Fail")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.title("Data Visualization of study hours vs Previous Score")
plt.grid(True)
plt.legend()
plt.show()

print(Border)
print("Step : 8")
print(Border,"\n")
print("Draw box plot for attendence. Identify if any outliiers are present.")

plt.figure(figsize=(8,6))
sns.boxplot(x = "Attendance",data=df)
plt.title("Data visualization of Box Plot ")
plt.show()

print(Border)
print("Step : 9")
print(Border,"\n")
print("Creat a plot which is showing relationship between assignments Completed and final result.")

plt.figure(figsize=(8,7))
sns.boxplot(x = "FinalResult",y="AssignmentsCompleted",hue = "FinalResult", palette={ 1 : 'g', 0 : 'r'},data=df)
plt.title("Relationship between Assignment Completed and final result")
plt.grid()
plt.show()

# plot sleep hours against final result 
print(Border)
print("Step : 9")
print(Border,"\n")

plt.figure(figsize=(9,6))
sns.boxplot(x="FinalResult", y="SleepHours",data = df, hue="FinalResult",palette={})
