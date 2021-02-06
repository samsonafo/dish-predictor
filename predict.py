import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import pickle
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from encoder import le

print("Loading model...")

# load the model from disk
filename = './models/nn_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

print("Model Loaded")
print(".")
print(".")
print(".")


#get input from user
img_add = input("Now input the path to your image: ")

#transform image into array
image_list = []
image_address = img_add

img = np.ravel(mpimg.imread(img_add))
image_list.append(img)
df_1 = pd.DataFrame(image_list)


#model prediction
arr = le.inverse_transform([np.argmax(loaded_model.predict(df_1))])

#print model result
for x in arr:
    print('This is {}. Enjoy your meal'.format(x))
