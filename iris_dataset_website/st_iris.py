import streamlit as st
import numpy as np
import pickle

st.title("Iris-specie Prediction App")
st.write("Please enter the data of flowers and ill predict its specie for you..")

sepal_l = st.number_input("Sepal Length: ", min_value = 0.0 )
sepal_w = st.number_input("Sepal width: ", min_value = 0.0 )
petal_l = st.number_input("Petal Length: ", min_value = 0.0 )
petal_w = st.number_input("Petal Width : ", min_value = 0.0 )

user_data= [[sepal_l,sepal_w,petal_l,petal_w]]

#model load for prediction
with open("model.pkl", "rb") as file:
    model=pickle.load(file)

#model.predict
if st.button("Predict"):
    pred=model.predict(user_data)
    st.write("The prediction specie is", pred[0])