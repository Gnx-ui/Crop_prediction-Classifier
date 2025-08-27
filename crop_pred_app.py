import numpy as np
import pickle as pkl
import streamlit as st


pickle_file=open("Crop_predictor.pkl","rb")
predictor=pkl.load(pickle_file)

""" # About:
         This Model is used to predict the type of plant to grow in place based on bio chemical and biophysical properties.
         The properties are Nitrogen,potassium,Phosphorus,Humidity etc.these fields are used to classify which type of crop 
         should be grown on that specific place so high yield can be achived in agricultural prospect.
    # input:
         please enter the test values in the predictors field.
    # Prediction:
         After giving the correct values in predictor field press the predict button.
         It will provide the type of crop to grow in the condition."""


def crop_prediction(N,P,K,temperature,humidity,ph,rainfall):
  features=np.array([[N,P,K,temperature,humidity,ph,rainfall]])
  return predictor.predict(features)

def main():
  st.title("crop_predictor")
  N=st.number_input("Nitrogen",min_value=0,max_value=150)
  P=st.number_input("Phosphorus",min_value=0,max_value=145)
  K=st.number_input("Potassium",min_value=8,max_value=205)
  temperature=st.number_input("Temperature",min_value=10,max_value=44)
  humidity=st.number_input("Humidity",min_value=14,max_value=100)
  ph=st.number_input("pH",min_value=3,max_value=10)
  rainfall=st.number_input("Rainfall",min_value=20,max_value=300)
  result=""
  if st.button("predict"):
    result=crop_prediction(N,P,K,temperature,humidity,ph,rainfall)
    st.success("The recommended crop is {}".format(result))

if __name__=='__main__':
  main()

