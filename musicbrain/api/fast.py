from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
from musicbrain.ml_logic.registry import load_model
from musicbrain.ml_logic.preprocessor import preprocess_features

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
def predict(
        pickup_datetime: str,
    ):
    """
    Make a single course prediction.
    Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
    """
    
    X_pred = pd.DataFrame(dict(

    ))
    
    X_processed = preprocess_features(X_pred)
    y_pred = app.state.model.predict(X_processed)
    
    return {"type_of_music": ""}


@app.get("/")
def root():
    return {"greeting": "Hello"}
