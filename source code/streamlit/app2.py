# DecissionTree
# file streamlit = app2.py 
# file model = dtree.joblib

import joblib
import streamlit as st

model_file = 'dtree.joblib'

# Memuat model dengan joblib.load
classifier = joblib.load(model_file)

st.set_page_config(page_title='ChurnPredictor', page_icon="🖖") 

@st.cache_data()
# Define the function which will make the prediction using data inputs from users
def prediction(seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines,
               internetservice, onlinesecurity, onlinebackup, deviceprotection, techsupport,
               streamingtv, streamingmovies, paperlessbilling, monthlycharges, M,
               one_year, two_year, credit_card, electronic_check, mailed_check):

    # Make predictions using the loaded model, not the array
    prediction_result = classifier.predict(
        [[seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines,
          internetservice, onlinesecurity, onlinebackup, deviceprotection, techsupport,
          streamingtv, streamingmovies, paperlessbilling, monthlycharges, M,
          one_year, two_year, credit_card, electronic_check, mailed_check]])

    if prediction_result == 0:
        pred = 'Everything Looks good. The Customer is Loyal!'
    else:
        pred = 'Oh No! The customer is gonna CHURN! **Better do something about it**'
    return pred

# This is the main function in which we define our webpage
def main():

    st.title("The Churn Predictor Model")   # Title of the model displayed in the webpage

    # Give a little bit information of the Model
    st.info('The Model takes in the below predictor variables for a telecom company and predicts if a customer is going to churn or not!', icon="ℹ️")

    # Create input fields
    seniorcitizen = st.number_input("Are you a senior citizen ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    partner = st.number_input("Do you have a partner ? ('1' for Yes and '0' for NO) ", min_value=0, max_value=1, value=0, step=1)
    dependents = st.number_input("Do you have any dependents ? ('1' for Yes and '0' for NO) ", min_value=0, max_value=1, value=0, step=1)
    tenure = st.number_input("Enter the months the customer (tenure) has stayed with the company(0-72)", min_value=0, max_value=72, value=10, step=3)
    phoneservice = st.number_input("Did the customer have a phone service ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    multiplelines = st.number_input("Did the customer have a multiplelines ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    internetservice = st.number_input("Did the customer have a internetservices ? ('N' : 0, 'DSL' : 2, 'FO (Fiber Optic)' : 2)", min_value=0, max_value=1, value=0, step=1)
    onlinesecurity = st.number_input("Did the customer have a onlinesecuritys ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    onlinebackup = st.number_input("Did the customer have a onlinebackup ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    deviceprotection = st.number_input("Did the customer have a deviceprotection ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    techsupport = st.number_input("Did the customer have a techsupport ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    streamingtv = st.number_input("Did the customer have a streamingtv ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    streamingmovies = st.number_input("Did the customer have a streamingmovies ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    paperlessbilling = st.number_input("Did the customer use paperless billing? ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    monthlycharges = st.number_input("Enter the monthlycharges the customer (0-118.75)", min_value=0.0, max_value=118.75, value=10.0, step=3.0)
    M = st.number_input("Are you a Male or Female ? ('1' for Male and '0' for Female)", min_value=0, max_value=1, value=0, step=1)
    one_year = st.number_input("Does the customer have One year contract ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    two_year = st.number_input("Does the customer have Two year contract ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    credit_card = st.number_input("Did the customer use Credit_card? ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    electronic_check = st.number_input("Did the customer use Electronic check ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)
    mailed_check = st.number_input("Did the customer use Mailed check ? ('1' for Yes and '0' for NO)", min_value=0, max_value=1, value=0, step=1)

    result = ""

    # When 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines,
                            internetservice, onlinesecurity, onlinebackup, deviceprotection, techsupport,
                            streamingtv, streamingmovies, paperlessbilling, monthlycharges, M,
                            one_year, two_year, credit_card, electronic_check, mailed_check)
        st.success(result)
        # If the predictions are true, celebrate that the model is properly working, else spit out a churn warning
        if result == 'Everything Looks good. The Customer is Loyal!':
            st.balloons()
        else:
            st.image('https://www.smartkarrot.com/wp-content/uploads/2020/09/Customer-churn-reduction.png',
                     caption="Customer CHURN ALERT", width=150)

if __name__ == '__main__':
    main()

