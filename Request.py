from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class weatherData(BaseModel):
    a : float 
    b : float 
    c : float 
    d : float
    e : float
    f : float