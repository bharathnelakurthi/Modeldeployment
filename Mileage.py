import pandas as pd
#import numpy as np
from sklearn.linear_model import LinearRegression


def Mileage_Prediction(Fuel):
    Data = pd.read_csv("/content/Deploy.csv")
    X = pd.DataFrame(data = Data['Fuel'])
    Y = pd.DataFrame(data = Data['Mileage'])

    Model = LinearRegression()
    Model.fit(X,Y)

    Test = pd.DataFrame(data = Fuel)

    return Model.predict(Test)


Mileage_Prediction()  
