# 1. Library imports
from pyexpat import model
import uvicorn
from fastapi import FastAPI
from Request import weatherData
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("model.pkl","rb")
model = pickle.load(pickle_in)

# Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_weather(data:weatherData):
    dataset = data.dict()
    A =dataset['a']
    B =dataset['b']
    C =dataset['c']
    D =dataset['d']
    E =dataset['e']
    F =dataset['f']

    Test_data = [[A,B,C,D,E,F]]
    Predicted_Value = model.predict(Test_data)
    Predict = Predicted_Value[0]
    return {
        'prediction': {'result':Predict}
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn Weather:app --reload