import streamlit as st
from utils import PrepProcesor, columns 
import tensorflow as tf
import numpy as np
import pandas as pd
import joblib
from PIL import Image
from prediction import predict
import os

@st.cache_data
def view_image(image_file):
    img = Image.open(image_file)
    return img

model = tf.saved_model.load('C:\\Users\\Piyush\\Desktop\\Classification Model(adhar+pan+passport)\\models\\1')

st.title('Found Something Suspicious!!')
st.subheader("Content Image")
main_image = st.file_uploader(
    "Upload Images", type=["png", "jpg", "jpeg"], key='main_image')

if main_image is not None:
    file_details = {"filename": main_image.name, "filetype": main_image.type,
                    "filesize": main_image.size}
    # st.write(file_details)
    st.image(view_image(main_image), width=400)
    with open(os.path.join(main_image.name), "wb") as f:
        f.write((main_image).getbuffer())

clicked = st.button('Check for oil spill')

if clicked:
    if main_image is not None:
        predictions = predict(
            os.path.join("images", main_image.name))
        st.write('### Output image:')
        st.markdown(predictions, unsafe_allow_html=True)
    else:
        st.write('Please Upload files properly')
# # PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# passengerid = st.text_input("Input Passenger ID", '123456') 
# pclass = st.selectbox("Choose class", [1,2,3])
# name  = st.text_input("Input Passenger Name", 'John Smith')
# sex = st.select_slider("Choose sex", ['male','female'])
# age = st.slider("Choose age",0,100)
# sibsp = st.slider("Choose siblings",0,10)
# parch = st.slider("Choose parch",0,2)
# ticket = st.text_input("Input Ticket Number", "12345") 
# fare = st.number_input("Input Fare Price", 0,1000)
# cabin = st.text_input("Input Cabin", "C52") 
# embarked = st.select_slider("Did they Embark?", ['S','C','Q'])

# def predict(): 
#     row = np.array([passengerid,pclass,name,sex,age,sibsp,parch,ticket,fare,cabin,embarked]) 
#     X = pd.DataFrame([row], columns = columns)
#     prediction = model.predict(X)
#     if prediction[0] == 1: 
#         st.success('Passenger Survived :thumbsup:')
#     else: 
#         st.error('Passenger did not Survive :thumbsdown:') 

# trigger = st.button('Predict', on_click=predict)