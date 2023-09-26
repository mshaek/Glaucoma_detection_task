# -*- coding: utf-8 -*-
"""Glaucoma_Detection_app.py

A Streamlit app created using the trained model



Original file is located at-
    https://colab.research.google.com/drive/1O1amCdBbjRcCHkk-HaUb8UzLiwkpuVlm
"""

# Importing the libraries and dependencies needed for creating the UI and supporting the deep learning models used in the project
import streamlit as st
import tensorflow as tf
import random
import cv2
from PIL import Image, ImageOps
import numpy as np

# hide deprication warnings which directly don't affect the working of the application
import warnings
warnings.filterwarnings("ignore")

# set some pre-defined configurations for the page, such as the page title, logo-icon, page loading state (whether the page is loaded automatically or you need to perform some action for loading)
st.set_page_config(
    page_title="Glaucome Detection App",
    page_icon = ":retina:",
    initial_sidebar_state = 'auto'
)

# hide the part of the code, as this is just for adding some custom CSS styling but not a part of the main idea
hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) # hide the CSS code from the screen as they are embedded in markdown text. Also, allow streamlit to unsafely process as HTML

def prediction_cls(prediction): # predict the class of the images based on the model results
    for key, clss in class_names.items(): # create a dictionary of the output classes
        if np.argmax(prediction)==clss: # check the class

            return key

with st.sidebar:
        st.image('retina.jpeg')
        st.title("Glaucoma Detection Automated")
        st.subheader("Welcome to the AI-powered Glaucoma Detection App! \n Simply upload an image of your retina to detect glaucoma with an accuracy of 51%.\n I made th This helps an user to easily detect the disease and identify its cause.\n Disclaimer: This is only a demo of the Glaucoma Detection App, and its accuracy is not guaranteed. It should not be used as a replacement for a medical diagnosis.")

st.write("""
         # Glaucoma Detection
         """
         )

file = st.file_uploader("", type=["jpg", "png"])
def import_and_predict(image_data, model):
        size = (299,299)
        # Read the input image.
        img = cv2.imread(image_data)

        # Resize the image to half its original size.
        resize_img = cv2.resize(img, size)

        img=cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
        #image = ImageOps.fit(img, size, Image.ANTIALIAS)
        #img = np.asarray(image)
        #img_reshape = img[np.newaxis,...]
        prediction = model.predict(img)
        return prediction


if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    # Get the probabilities of the prediction.
    probabilities = predictions[0]
    st.sidebar.error("Accuracy : " + probabilities + " %")

    class_names = ["Glaucoma", "sanas"]

    string = "Detected Disease : " + class_names[np.argmax(predictions)]
    if class_names[np.argmax(predictions)] == 'Glaucoma':
        st.balloons()
        st.sidebar.success(string)

    elif class_names[np.argmax(predictions)] == 'sanas':
        st.sidebar.warning(string)
        st.markdown("## display")
        st.info("Test result shows no sign of glaucoma. Please take good care of your eyes.")
