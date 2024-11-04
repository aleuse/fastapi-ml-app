from fastapi import FastAPI
from pydantic import BaseModel
from utils import load_models, make_prediction

model, label_encoders, scaler = load_models()
app = FastAPI()

class InputData(BaseModel):
    Age: str
    EdLevel: str
    Employment: int
    Gender: str
    MentalHealth: str
    MainBranch: str
    YearsCode: int
    YearsCodePro: int
    Country: str
    PreviousSalary: float
    ComputerSkills: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

@app.post("/predict")
def predict(data: InputData):
    prediction = make_prediction(data, model, label_encoders, scaler)
    return {"prediction": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)