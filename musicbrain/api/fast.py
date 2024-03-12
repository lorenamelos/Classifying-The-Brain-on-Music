import io
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd

from musicbrain.ml_logic.model import int_to_music_label
from musicbrain.ml_logic.registry import load_model

app = FastAPI()
app.state.model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
async def predict(file: UploadFile = File(None), json_data: dict = None):
    
    if file and file.filename.endswith((".csv")):
        contents = await file.read()
        
        try:
            X_pred = pd.read_csv(io.BytesIO(contents))
            y_pred = app.state.model.predict(X_pred)
            
            result = int_to_music_label(y_pred)
            return {"music_labels": result}
        except Exception as e:
            return {"error": f"Invalid CSV file, exception '{e}'"}

    elif json_data:
        try:
            X_pred = pd.read_json(json_data)
            y_pred = app.state.model.predict(X_pred)
            
            result = int_to_music_label(y_pred)
            return {"music_labels": result}
        except Exception as e:
            return {"error": f"Invalid JSON, exception '{e}'"}
        
    else:
        return {"error": "No valid input provided"}
