import streamlit as st
import base64
import sklearn
import numpy as np
import pickle as pkl

#Load the saved model
model = pkl.load(open("model.p","rb"))


# Page configs:
st.set_page_config(page_title="Stroke Prediction App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")



def preprocess(gender, age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoke, Residence_type):
    ''' This function converts user input to the variables for the model.
    Parameters:
        gender, age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoke, Residence_type: input provided by user
    Returns:
        prediction:  0 or 1 
    '''

 
    if gender=="Male":
        gender = 1 
    else: gender = 0
    
    if hypertension == "Yes":
        hypertension = 1
    else: hypertension = 0

    if heart_disease == "Yes":
        heart_disease = 1
    else: heart_disease = 0

    if ever_married == "Yes":
        ever_married = 1
    else: ever_married = 0

    if work_type == "Goverment job":
        Goverment_job = 1
        Never_worked = 0
        Parental_leave = 0
        Private = 0
        Self_employed = 0
    elif work_type == "Private company":
        Goverment_job = 0
        Never_worked = 0
        Parental_leave = 0
        Private = 1
        Self_employed = 0
    elif work_type == "Never worked":
        Goverment_job = 0
        Never_worked = 1
        Parental_leave = 0
        Private = 0
        Self_employed = 0
    elif work_type == "Self-employed":
        Goverment_job = 0
        Never_worked = 0
        Parental_leave = 0
        Private = 0
        Self_employed = 1    
    else:
        Goverment_job = 0
        Never_worked = 0
        Parental_leave = 1
        Private = 0
        Self_employed = 0
        
    if smoke == "Yes":
        formerly_smoked = 0
        never_smoked = 0
        smokes = 1
    elif smoke == "Former smoker":   
        formerly_smoked = 1
        never_smoked = 0
        smokes = 0
    elif smoke == "Never smoked":   
        formerly_smoked = 0
        never_smoked = 1
        smokes = 0
    else:
        formerly_smoked = 0
        never_smoked = 0
        smokes = 0

    if Residence_type == "Urban":
        Residence_type = 1
    else:
        Residence_type = 0
        
        


    model_input = [gender, age, hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, Goverment_job, Never_worked, Parental_leave, Private, Self_employed, formerly_smoked, never_smoked, smokes]
    model_input = np.array(model_input)
    model_input = model_input.reshape(1,-1)
    prediction = model.predict(model_input)

    return prediction

    

       
# Elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Stroke Prediction App</h1> 
    </div> 
    """
      
st.markdown(html_temp, unsafe_allow_html = True) 

      
# Create the boxes and sliders for entering data:

age = st.slider("Your age", min_value = 0, max_value= 100)
gender = st.radio("Select gender: ", ('Male', 'Female'))
hypertension = st.radio("Do you have hypertension? ", ('Yes', 'No'))
heart_disease = st.radio("Do you have heart diseases? ", ('Yes', 'No'))
avg_glucose_level = st.slider('Blood sugar in mg/dl; if you do not know this value, set to 75',  min_value=40, max_value=300)
bmi = st.slider('Your body mass index; if you do not know this value, set to 20', min_value=10, max_value=100)
smoke = st.selectbox('Are you a smoker?', ("Yes", "Former smoker", "Never smoked", "I do not know"))
ever_married = st.radio("Are you married / ever been married?", ('Yes', 'No'))
work_type = st.selectbox('Type of your work: ', ("Goverment job", "Private company", "Self-employed", "Never worked", "On parental leave"))
Residence_type = st.selectbox('You residence type: ', ("Urban", "Rural"))

# Print user input and prediction in console:
print(gender, age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoke, Residence_type)
pred = preprocess(gender, age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, bmi, smoke, Residence_type)
print (pred)



# Button:
if st.button("Get my prediction!"):    
  if pred[0] == 1:
    st.error('You have high risk of getting a stroke!')
    st.info("Caution: Please, remember that this is just an app. Consult with your doctor!") 
    
  else:
    st.success('You have low risk of getting a stroke!')
    st.info("Caution: Please, remember that this is just an app. Consult with your doctor!") 
   


# Info in sidebar:
st.sidebar.subheader("About App")
st.sidebar.image("https://cdn.pixabay.com/photo/2018/02/20/17/33/brain-3168269_1280.png")
st.sidebar.info("This app helps you to find out whether you are at risk of developing a stroke.")
st.sidebar.info("Fill all the fields and click on the button.")
