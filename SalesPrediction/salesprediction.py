# -*- coding: utf-8 -*-
"""SalesPrediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18D1ChL9YSwEeu1wycdXDGcM9Ey1TQ9LW
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Advertising.csv')

df.head()

df.shape

df.info()

df.duplicated().sum()

X=df.drop('Sales',axis=1)
y=df['Sales']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size = 0.30, random_state = 1)

from sklearn.linear_model import LinearRegression
Lr= LinearRegression()

Lr.fit(X_train,y_train)

Lr.score(X_train,y_train)

y_pred=Lr.predict(X_test)

y_pred

plt.scatter(y_test,y_pred,color='r')