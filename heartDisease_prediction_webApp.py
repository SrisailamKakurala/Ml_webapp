
import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('m.sav', 'rb'))


def predict(input_data):
    input_data = np.array(input_data)

    # we need to reshape cos we need to tell model that
    # we are predicting for only one value not for whole
    # dataset
    input_data = input_data.reshape(1,-1)

    prediction = model.predict(input_data)

    # 0 -> no disease
    # 1 -> disease
    if(prediction[0] == 0): return "The person has NO heart disease"
    else: return "The person has heart disease"
    
    
    

def main():
    
    # giving title to the web app
    st.title("heart disease prediction web app")
    
    # getting the input data from user
    age = st.text_input("Enter age: ")
    sex = st.text_input("Enter sex: ")
    cp = st.text_input("Enter cp: ")
    trestbps = st.text_input("Enter trestbps: ")
    chol = st.text_input("Enter chol: ")
    fbs = st.text_input("Enter fbs: ")
    restecg = st.text_input("Enter restecg: ")
    thalach = st.text_input("Enter thalach: ")
    exang = st.text_input("Enter exang: ")
    oldpeak = st.text_input("Enter oldpeak: ")
    slope = st.text_input("Enter slope: ")
    ca = st.text_input("Enter ca: ")
    thal = st.text_input("Enter thal: ")
    
    # # Convert inputs to appropriate types
    # casted_data = [
    #     float(age),
    #     float(sex),
    #     float(cp),
    #     float(trestbps),
    #     float(chol),
    #     float(fbs),
    #     float(restecg),
    #     float(thalach),
    #     float(exang),
    #     float(oldpeak),
    #     float(slope),
    #     float(ca),
    #     float(thal)
    # ]
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Diabetes Test Results'):
        diagnosis = predict([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    
    st.success(diagnosis)
    

if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
