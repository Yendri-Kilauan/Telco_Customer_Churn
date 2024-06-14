# Test ke FastAPI
# nama file : app.py
# Port : http://127.0.0.1:8000
# Pengetesan : http://127.0.0.1:8000/docs


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

# Load the model
model_file = 'logistic.joblib'
classifier = joblib.load(model_file)

app = FastAPI(title='Churn Predictor API', description='API untuk memprediksi customer churn', version='1.0')

# Define the request body structure
class ChurnRequest(BaseModel):
    seniorcitizen: int
    partner: int
    dependents: int
    tenure: int
    phoneservice: int
    multiplelines: int
    internetservice: int
    onlinesecurity: int
    onlinebackup: int
    deviceprotection: int
    techsupport: int
    streamingtv: int
    streamingmovies: int
    paperlessbilling: int
    monthlycharges: float
    M: int
    one_year: int
    two_year: int
    credit_card: int
    electronic_check: int
    mailed_check: int

# Define the prediction function
def make_prediction(data: ChurnRequest):
    features = [[
        data.seniorcitizen, data.partner, data.dependents, data.tenure, data.phoneservice, data.multiplelines,
        data.internetservice, data.onlinesecurity, data.onlinebackup, data.deviceprotection, data.techsupport,
        data.streamingtv, data.streamingmovies, data.paperlessbilling, data.monthlycharges, data.M,
        data.one_year, data.two_year, data.credit_card, data.electronic_check, data.mailed_check
    ]]
    
    prediction = classifier.predict(features)

    if prediction == 0:
        return 'Everything Looks good. The Customer is Loyal!'
    else:
        return 'Oh No! The customer is gonna CHURN! **Better do something about it**'

@app.post('/predict')
def predict_churn(data: ChurnRequest):
    try:
        result = make_prediction(data)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Main route
@app.get('/')
def read_root():
    return {"message": "Welcome to the Churn Predictor API"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
