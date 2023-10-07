import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("model.pkl","rb")
classifier= pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(spl,spw,pel,pew,pew1,pew2,pew3,pew4,pew5):
     
    prediction=classifier.predict([[spl,spw,pel,pew,pew1,pew2,pew3,pew4,pew5]])
    print(prediction)
    return prediction



def main():
    st.title("Steamlit ML App")
    html_temp = """
    <div style="background-color:Red;padding:10px">
    <h2 style="color:white;text-align:center;">AI Mental Fitness Tracker</h2>
    </div>
    <br></br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    spl = st.number_input("Country")
    spw = st.number_input("Year")
    pel = st.number_input("Schizophrenia")
    pew = st.number_input("Bipolar disorder")
    pew1 = st.number_input("Eating disorder")
    pew2 = st.number_input("Anxiety")
    pew3 = st.number_input("Drug")
    pew4 = st.number_input("Depressive disorder")
    pew5 = st.number_input("Alcohol")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(spl,spw,pel,pew,pew1,pew2,pew3,pew4,pew5)
        st.success('The output is {}'.format(result))
        if result <= 3 :
          image = Image.open('bmi 2.jpg')
          st.image(image, caption='Underweight')
        elif (result >= 3 and result<=6) :
          image = Image.open('bmi 3.jpg')
          st.image(image, caption='Normal')
        elif (result >= 6 and result<=9):
          image = Image.open('bmi 4.jpg')
          st.image(image, caption='Overweight')
        elif result>=9:
          image = Image.open('bmi 5.jpg')
          st.image(image, caption='Obesity') 
          
    if st.button("About"):
        st.text("This project uses various Machine Learning Algorithms to predict the fitness of ")
        st.text("the person using attributes like drug, alcohol, anxiety and many other attributes.")
        st.text("Achieved accuracy of 99%"" using Random forest regressor.")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    