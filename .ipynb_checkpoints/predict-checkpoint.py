import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from encoder import le
from PIL import Image

import warnings
warnings.filterwarnings("ignore")

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

img = Image.open(img_add)
img = img.resize((170,140),Image.ANTIALIAS) #reduce image size to accomodata all images

img = np.ravel(img)
image_list.append(img)
df_1 = pd.DataFrame(image_list)

print('Now Making prediction...')

#model prediction
arr = le.inverse_transform([np.argmax(loaded_model.predict(df_1))])

#print model result
for x in arr:
    print('This is {}. Enjoy your meal'.format(x))
