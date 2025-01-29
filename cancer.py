# Import All Necessary Libraries
import joblib # type: ignore
import streamlit as st # type: ignore
import warnings
warnings.filterwarnings("ignore")
# Uploading the model
model = joblib.load("randomforest.joblib") 
st.header("Cancer Predictor")
col1, col2, col3 = st.columns(3)
with col1:
    Age = st.text_input("Age")
    Gender = st.number_input("Gender", min_value = 0, max_value = 1)     
    Smoking = st.number_input("Smoking", min_value = 0, max_value = 1)
    Hx_Smoking = st.number_input("Hx_Smoking", min_value = 0, max_value = 1)
    Hx_Radiothreapy = st.number_input("Hx_Radiothreapy", min_value = 0, max_value = 1)
    
with col2:
    Physical_Examination = st.number_input("Physical_Examination", min_value = 0, max_value = 5)
    Adenopathy = st.number_input("Adenopathy", min_value = 0, max_value = 5)
    Pathology = st.number_input("Pathology", min_value = 0, max_value = 3)
    Focality = st.number_input("Focality", min_value = 0, max_value = 1)
    Risk = st.number_input("Risk", min_value = 0, max_value = 2)
    Response = st.number_input("Response", min_value = 0, max_value = 3)
with col3:
    Clinical_Hyperthyroidism = st.number_input("Clinical_Hyperthyroidism", min_value = 0, max_value = 1)
    Clinical_Hypothyroidism = st.number_input("Clinical_Hypothyroidism", min_value = 0, max_value = 1)
    Euthyroid = st.number_input("Euthyroid", min_value = 0, max_value = 1)
    Subclinical_Hyperthyroidism = st.number_input("Subclinical_Hyperthyroidism", min_value = 0, max_value = 1)
    Subclinical_Hypothyroidism = st.number_input("Subclinical_Hypothyroidism", min_value = 0, max_value = 1)

if st.button("Prediction"):
    predict = model.predict([[Age, Gender, Smoking, Hx_Smoking, Hx_Radiothreapy, Physical_Examination, Adenopathy,
                                     Pathology, Focality, Risk, Response, Clinical_Hyperthyroidism,
                                     Clinical_Hypothyroidism, Euthyroid, Subclinical_Hyperthyroidism, Subclinical_Hypothyroidism]])
    st.success(predict[0])
    st.write("If prediction is 0 cancer is likely not to reoccur, but if 1 cancer is likely to reoccur")
