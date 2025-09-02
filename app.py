import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
import joblib


model = joblib.load("CBC.pkl")


st.title("Customer Churn Analysis")
gender = st.selectbox("select gender", ['Female', 'Male'])
SeniorCitizen = st.number_input("Senior Citizen ", min_value=0)
Partner = st.selectbox('select Partner', ['Yes', 'No'])
Dependents = st.selectbox('select dependents', ['No', 'Yes'])
tenure = st.number_input('tenure', min_value=0)
PhoneService = st.selectbox('select Phone Service', ['No', 'Yes'])
MultipleLines = st.selectbox('MultipleLines ',['No phone service', 'No', 'Yes'])
InternetService = st.selectbox("InternetService",['DSL', 'Fiber optic', 'No'])
OnlineSecurity = st.selectbox('OnlineSecurity', ['No', 'Yes', 'No internet service'])
OnlineBackup = st.selectbox('OnlineBackup', ['Yes', 'No', 'No internet service'])
DeviceProtection = st.selectbox('DeviceProtection', ['No', 'Yes', 'No internet service'])
TechSupport = st.selectbox('TechSupport', ['No', 'Yes', 'No internet service'])
StreamingTV = st.selectbox('StreamingTV', ['No', 'Yes', 'No internet service'])
StreamingMovies = st.selectbox('StreamingMovies', ['No', 'Yes', 'No internet service'])
Contract =  st.selectbox('Contract',['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox('PaperlessBilling', ['Yes', 'No'])
PaymentMethod = st.selectbox('PaymentMethod',['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'])
MonthlyCharges = st.number_input('MonthlyCharges', min_value=0.0)
TotalCharges = st.number_input('TotalCharges', min_value=0.0)

if gender == 'Female':
    gender = 0
else:
    gender = 1

if Partner == 'Yes':
    Partner = 0
else:
    Partner = 1

if Dependents=='No':
    Dependents = 0
else:
    Dependents=1

if PhoneService == 'No':
    PhoneService = 0
else:
    PhoneService = 1

if MultipleLines == 'No phone service' :
    MultipleLines = 0
elif MultipleLines =='No':
    MultipleLines = 1
else:
    MultipleLines = 2

if InternetService == 'DSL':
    InternetService = 0
elif InternetService == 'Fiber optic':
    InternetService = 1
else:
    InternetService = 2

if OnlineSecurity == 'Yes':
    OnlineSecurity = 0
elif OnlineSecurity == 'No':
    OnlineSecurity = 1
else:
    OnlineSecurity = 2


if OnlineBackup == 'Yes':
    OnlineBackup = 0
elif OnlineBackup == 'No':
    OnlineBackup = 1
else:
    OnlineBackup = 2

if DeviceProtection == 'No':
    DeviceProtection = 0
elif DeviceProtection == 'Yes':
    DeviceProtection = 1
else:
    DeviceProtection = 2

if TechSupport == 'No':
    TechSupport = 0
elif TechSupport == 'Yes':
    TechSupport = 1
else:
    TechSupport = 2

if StreamingTV == 'No':
    StreamingTV = 0
elif StreamingTV == 'Yes':
    StreamingTV = 1
else:
    StreamingTV = 2

if StreamingMovies == 'No':
    StreamingMovies = 0
elif StreamingMovies == 'Yes':
    StreamingMovies = 1
else:
    StreamingMovies = 2

if Contract == 'Month-to-month':
    Contract = 0
elif Contract == 'One year':
    Contract = 1
else:
    Contract = 2

if PaperlessBilling == 'No':
    PaperlessBilling = 0
else:
    PaperlessBilling = 1

if PaymentMethod == 'Electronic check':
    PaymentMethod =0
elif PaymentMethod == 'Mailed check':
    PaymentMethod = 1
elif PaymentMethod == 'Bank transfer (automatic)':
    PaymentMethod =2
else:
    PaymentMethod = 3


if st.button('Predict'):
    input_data = pd.DataFrame([{
        'gender':gender,
        'SeniorCitizen':SeniorCitizen,
        'Partner':Partner,
        'Dependents':Dependents,
        'tenure':tenure,
        'PhoneService':PhoneService,
        'MultipleLines':MultipleLines,
        'InternetService':InternetService,
        'OnlineSecurity':OnlineSecurity,
        'OnlineBackup':OnlineBackup,
        'DeviceProtection':DeviceProtection,
        'TechSupport':TechSupport,
        'StreamingTV':StreamingTV,
        'StreamingMovies':StreamingMovies,
        'Contract':Contract,
        'PaperlessBilling':PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges':MonthlyCharges,
        'TotalCharges':TotalCharges,
    }])

    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error('Customer is churned')
    else:
        st.success('Customer is going to churn')








# gender
# ['Female' 'Male'] [0, 1]
# **************************************************
# Partner
# ['Yes' 'No'] [0, 1]
# **************************************************
# Dependents
# ['No' 'Yes'] [0, 1]
# **************************************************
# PhoneService
# ['No' 'Yes'] [0, 1]
# **************************************************
# MultipleLines
# ['No phone service' 'No' 'Yes'] [0, 1, 2]
# **************************************************
# InternetService
# ['DSL' 'Fiber optic' 'No'] [0, 1, 2]
# **************************************************
# OnlineSecurity
# ['No' 'Yes' 'No internet service'] [0, 1, 2]
# **************************************************
# OnlineBackup
# ['Yes' 'No' 'No internet service'] [0, 1, 2]
# **************************************************
# DeviceProtection
# ['No' 'Yes' 'No internet service'] [0, 1, 2]
# **************************************************
# TechSupport
# ['No' 'Yes' 'No internet service'] [0, 1, 2]
# **************************************************
# StreamingTV
# ['No' 'Yes' 'No internet service'] [0, 1, 2]
# **************************************************
# StreamingMovies
# ['No' 'Yes' 'No internet service'] [0, 1, 2]
# **************************************************
# Contract
# ['Month-to-month' 'One year' 'Two year'] [0, 1, 2]
# **************************************************
# PaperlessBilling
# ['Yes' 'No'] [0, 1]
# **************************************************
# PaymentMethod
# ['Electronic check' 'Mailed check' 'Bank transfer (automatic)'
#  'Credit card (automatic)'] [0, 1, 2, 3]