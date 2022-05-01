from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class weatherData(BaseModel):
    Temperature : float 
    Apparent_Temp : float 
    Wind_Speed : float 
    Wind_Bearing : float
    Visibility : float
    Pressure : float