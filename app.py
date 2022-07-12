import streamlit as st
import pickle
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title = None,
    options = ["Home","Predict","About"], 
    icons = ["house","speedometer","person"], 
    menu_icon = "menu-button", 
    orientation = "horizontal",
)

if selected == "Home":
    with st.container():
        st.title('Medical Insurance Predictor!')
        st.subheader('By Anirudh :wave:')
    with st.container():
        st.title('Predict your insurance cost :information_source:')
        st.write('The insurance predicor is not super accurate by you can get the basic idea of how much it will cost you. Insurance cost are extremely expensive these days and the differ from person to person so this app helps to curate the insurance cost for you.')
        st.subheader('Disclaimer :heavy_exclamation_mark:')
        st.write('The predicted cost may be more or less compared with the true cost. Remember that this is just for a idea.')
        st.subheader('This is a sample Dataset:')
        df = pd.read_csv("Medicalpremium.csv")
        st.write(df)


if selected == "Predict":
    st.title('Predict your insurance cost')
    st.subheader('Enter the details')
    model = pickle.load(open('randomforestregressor.sav','rb'))
    
    def mip(input_data):
        na = np.asarray(input_data)
        d = na.reshape(1,-1)
        
        prediction = model.predict(d)
        return prediction


    def main():

        Age = st.text_input('Age')
        Diabetes1 = st.selectbox('Diabetes',('Yes','No'))
        BloodPressureProblems1 = st.selectbox('Blood Pressure Problems',('Yes','No'))
        AnyTransplants1 = st.selectbox('Any Transplants',('Yes','No'))
        AnyChronicDiseases1 = st.selectbox('Any Chronic Diseases',('Yes','No'))
        Height = st.text_input('Height in Cm')
        Weight = st.text_input('Weight in Kg')
        KnownAllergies1 = st.selectbox('Known Allergies',('Yes','No'))
        HistoryOfCancerInFamily1  = st.selectbox('History Of Cancer In Family ',('Yes','No'))
        NumberOfMajorSurgeries = st.text_input('NumberOfMajorSurgeries')

        #Diabetes
        if Diabetes1 == 'Yes':
           Diabetes = 1
        else:
           Diabetes = 0    

        #BloodPressureProblems
        if BloodPressureProblems1 == 'Yes':
           BloodPressureProblems = 1
        else:
           BloodPressureProblems = 0  

        #AnyTransplants
        if AnyTransplants1 == 'Yes':
           AnyTransplants = 1
        else:
           AnyTransplants = 0  

         #AnyChronicDiseases
        if AnyChronicDiseases1 == 'Yes':
           AnyChronicDiseases = 1
        else:
           AnyChronicDiseases = 0  

         #KnownAllergies
        if KnownAllergies1 == 'Yes':
           KnownAllergies = 1
        else:
           KnownAllergies = 0

         #HistoryOfCancerInFamily
        if HistoryOfCancerInFamily1 == 'Yes':
           HistoryOfCancerInFamily = 1
        else:
           HistoryOfCancerInFamily = 0      

        Medical_Insurance = ''
        if st.button('Get cost'):
            Medical_Insurance  = mip([Age, Diabetes ,BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies, HistoryOfCancerInFamily, NumberOfMajorSurgeries])  
        st.success(Medical_Insurance)


    if __name__ == '__main__':
        main()

if selected == "About":
    #st.title('About')
    st.title('Hi, Anirudh here :smiley:')
    st.subheader('Hope this app was useful to you :innocent:')
    st.write('I am a student as of now who is passionate about Data Science and this is a insurance prdictor which uses linear regression to predict the cost of the insurance but the model accuracy is low ie 0.7454474167181153 so it is not exact but it is enough to get a idea. see the sample dataset to know how to fill in details.')
    st.write('[More projects in GITHUB >](https://github.com/4nirudh5)')
