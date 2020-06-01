from tkinter import *
import pandas as pd
from sklearn.tree import  tree
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import sqlite3
#import getpass
#import Login as log


def machineLearning(user,name,avoidEye, vibrates, response, realize, space, deaf, inappropriate,repeatedly, unemotional, constant, age, jundice, autism):

    dataset =pd.read_csv('data.csv')
    #pd.set_option('display.max_rows', None) #for printing
    #pd.set_option('display.max_columns',14)#for printing
    #print(dataset)
    #print(dataset.describe())

    y=dataset.Class
    x=dataset.drop('Class',axis=1)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state = 1)
    #print("X_train: ",X_train.shape)
    #print("y_train: ",y_train.shape)
   # print("X_test: ",X_test.shape)
    #print("y_test: ",y_test.shape)

    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, clf.predict(X_test))
    # print('-' * 10)
    # print(f'Accuracy of (DecisionTreeClassifier) is: {round(accuracy * 100, 2)}%')
    # print('-' * 10)

    prediction=clf.predict(X_test)
    # for i in range (0,10):
    #     print("Actual outcome: {} and predicted outcome: {}".format(list(y_test)[i],prediction[i]))
    # print("Train accuracy:", accuracy_score(y_train,clf.predict(X_train)))
    # print("Test accuracy:", accuracy_score(y_test,prediction))


    # print("the test data \n", X_test)
    # print("enter one row from the testing data to make the machine guess the performance:")
    # age=input("Enter age:")
    # avoidEye=input("Does the person avoid meeting eyes? [1 yes - 0 no]: ")
    # vibrates=input("Does the person vibrates forward and backward while standing and sitting? [1 yes - 0 no]: ")
    # response= input("Is the person's response inappropriate for simple orders? [1 yes - 0 no]: ")
    # realize=input("Does the person realize the presence of people around him/her? [1 yes - 0 no]: ")
    # space=input("does the person look at the vast space a lot? [1 yes - 0 no]: ")
    # deaf=input("Does the person seem deaf to some voices while responding to other voices? [1 yes - 0 no]: ")
    # inappropriate=input("Does the person use inappropriate pronouns? [1 yes - 0 no]: ")
    # repeatedly=input("Does the person do things repeatedly as if they were rituals? [1 yes - 0 no]: ")
    # unemotional=input("Is the person unemotional or unfriendly,  does not give an emotional response to hugs or kisses? [1 yes - 0 no]: ")
    # constant=input("Does the person make constant gestures and signals? [1 yes - 0 no]: ")
    # jundice=input("Is jundice? [1 yes - 0 no]: ")
    # autism=input("Is autism? [1 yes - 0 no]: ")
    m = clf.predict([[avoidEye, vibrates, response, realize, space, deaf, inappropriate,repeatedly, unemotional, constant, age, jundice, autism]])
    print("name: ", name,"result: ",m)
    #print(getpass.getuser())

    #log = Login
    conn=sqlite3.connect("DBMAs.db")
    c=conn.cursor()
        # c.execute("INSERT INTO CHILD WHERE (username = '"  +str(fusernamd.get()) + "')")
    c.execute("INSERT INTO CHILD VALUES('"+str(user)+"' ,'" +str(name)+"', '"+str(age)+"','"+str(m)+"' )")
    conn.commit()
    conn.close()
    #print("check if correct or not:\n",y_test)