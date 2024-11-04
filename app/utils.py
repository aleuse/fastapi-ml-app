import pickle
import pandas as pd
import os

root_dir = os.path.dirname(os.path.abspath(__file__))

def load_models():
    # Cargar el modelo y los LabelEncoders
    with open(os.path.join(root_dir, 'models/best_model.pkl'), 'rb') as model_file:
        model = pickle.load(model_file)

    with open(os.path.join(root_dir, 'models/label_encoders.pkl'), 'rb') as le_file:
        label_encoders = pickle.load(le_file)

    with open(os.path.join(root_dir, 'models/scaler.pkl'), 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    
    return model, label_encoders, scaler

def make_prediction(data, model, label_encoders, scaler):
    # Convertir los datos de entrada a un DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Aplicar Label Encoding a las columnas categóricas
    for col, le in label_encoders.items():
        input_df[col] = le.transform(input_df[col])

    # Escalar los datos
    input_scaled = scaler.transform(input_df)

    # Hacer la predicción
    prediction = model.predict(input_scaled)
    
    return {"prediction": int(prediction[0])}
