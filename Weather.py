# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Request import weatherData
import pickle

# 2. Create the app object and load the pickel file
app = FastAPI()
pickle_in = open("model.pkl","rb")
model = pickle.load(pickle_in)

# 3. Expose the prediction functionality, make a prediction from the passed
# JSON data and return the predicted Humidity Percentage
@app.get('/')
def Home():
    return{
        '/Predict should be the api endpoint for predicting Humidity'
    }
@app.post('/predict')
def predict_weather(data:weatherData):
    dataset = data.dict()
    A =dataset['Temperature']
    B =dataset['Apparent_Temp']
    C =dataset['Wind_Speed']
    D =dataset['Wind_Bearing']
    E =dataset['Visibility']
    F =dataset['Pressure']

    Test_data = [[A,B,C,D,E,F]]
    Predicted_Value = model.predict(Test_data)
    Predict = Predicted_Value[0]
    Format_Predict = "{:.2f}".format(Predict)
    Format_Predict = float(Format_Predict)*100
    if(A>=0 and A<0.2):
        band = 'BNAD - A'
    elif(A>=0.2 and A<0.4):
        band = 'BNAD - B'
    elif(A>=0.4 and A<0.6):
        band = 'BNAD - C'
    elif(A>=0.6 and A<0.8):
        band = 'BNAD - D'
    elif(A>=0.8 and A<1.0):
        band = 'BNAD - E'
    return {
        'prediction': {'Humidity (%)':Format_Predict,
                       'Music Band':band}
    }

# 4. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn Weather:app --reload