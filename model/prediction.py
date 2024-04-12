import tensorflow as tf
import numpy as np
import cv2 as cv

model = tf.saved_model.load('C:\\Users\\Piyush\\Desktop\\Classification Model(adhar+pan+passport)\\models\\1')

class_names=['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
def predict(img_path):
    print('hello', img_path)
    img=cv.imread(img_path)
    img= cv.resize(img, [320, 320]) 
    img_array= tf.keras.preprocessing.image.img_to_array(img)
    img_array= tf.expand_dims(img_array, 0)

    predictions= model.predict(img_array)

    predicted_class=class_names[np.argmax(predictions[0])]
    confidence= round(100*(np.max(predictions[0])), 2)
    return predicted_class, confidence