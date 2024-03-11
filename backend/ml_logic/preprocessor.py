import numpy as np
import pandas as pd

from sklearn.decomposition import PCA

def preprocess_features(X: pd.DataFrame) -> np.ndarray:
    
    print("\nPreprocessing features...")
     
    pca = PCA(n_components=90)
    X_processed = pca.fit_transform(X)
     
    print("✅ X_processed, with shape", X_processed.shape)
    
    return X_processed