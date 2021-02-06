import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('./data/new_train.csv',index_col=0)
test = pd.read_csv('./data/new_test.csv',index_col=0)

le = LabelEncoder()  #instantiate the label encoder
 
y_train = le.fit_transform(train['name_of_dish'])
y_test = le.transform(test['name_of_dish'])


