import glob
import os
import time
from musicbrain.params import *
from colorama import Fore, Style
from google.cloud import storage
import joblib
import mlflow
from sklearn.linear_model import LogisticRegression

def load_model(stage="Production") -> LogisticRegression:
    """
    Return a saved model:
    - locally (latest one in alphabetical order)
    - or from GCS (most recent one) if MODEL_TARGET=='gcs'  --> for unit 02 only
    - or from MLFLOW (by "stage") if MODEL_TARGET=='mlflow' --> for unit 03 only
    Return None (but do not Raise) if no model is found
    """
    if MODEL_TARGET == "local":
        print(Fore.BLUE + f"\nLoad latest model from local registry..." + Style.RESET_ALL)
        # Get the latest model version name by the timestamp on disk
        local_model_directory = os.path.join(MODEL_LOCAL_REGISTRY_PATH, "models")
        local_model_paths = glob.glob(f"{local_model_directory}/*")
        if not local_model_paths:
            return None
        most_recent_model_path_on_disk = sorted(local_model_paths)[-1]
        print(Fore.BLUE + f"\nLoad latest model from disk..." + Style.RESET_ALL)
        latest_model = joblib.load(most_recent_model_path_on_disk)
        print(":marca_de_verificação_branca: Model loaded from local disk")
        return latest_model

    elif MODEL_TARGET == "gcs":
        # :presente: We give you this piece of code as a gift. Please read it carefully! Add a breakpoint if needed!
        print(Fore.BLUE + f"\nLoad latest model from GCS..." + Style.RESET_ALL)
        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)
        blobs = bucket.list_blobs(prefix="models/")
        model_path_folder = os.path.join(MODEL_LOCAL_REGISTRY_PATH, "models")
        create_folder_if_not_exist(model_path_folder)
        try:
            latest_blob = max(blobs, key=lambda x: x.updated)
            latest_model_path_to_save = os.path.join(MODEL_LOCAL_REGISTRY_PATH, latest_blob.name)

            latest_model = None
            if os.path.exists(latest_model_path_to_save):
                print("Latest model already exists locally. Returning...")
                latest_model = joblib.load(latest_model_path_to_save)
            else:
                latest_blob.download_to_filename(latest_model_path_to_save)
                latest_model = joblib.load(latest_model_path_to_save)
                print(":marca_de_verificação_branca: Latest model downloaded from cloud storage")
            return latest_model
        except Exception as e:
            print(f"\n❌ No model found in GCS bucket {BUCKET_NAME} /n exception: ${e}")
            return None
    elif MODEL_TARGET == "mlflow":
        print(Fore.BLUE + f"\nLoad [{stage}] model from MLflow..." + Style.RESET_ALL)
        # Load model from MLflow
        model = None
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        client = mlflow.tracking.MlflowClient()
        try:
            model_versions = client.get_latest_versions(name=MLFLOW_MODEL_NAME, stages=[stage])
            model_uri = model_versions[0].source
            assert model_uri is not None
        except:
            print(f"\n:x_vermelho: No model found with name {MLFLOW_MODEL_NAME} in stage {stage}")
            return None
        model = mlflow.tensorflow.load_model(model_uri=model_uri)
        print(":marca_de_verificação_branca: Model loaded from MLflow")
        return model
    else:
        print("No Model found")
        return None
def save_model(model: LogisticRegression = None) -> None:
    """
    Persist trained model locally on the hard drive at f"{LOCAL_REGISTRY_PATH}/models/{timestamp}.h5"
    - if MODEL_TARGET='gcs', also persist it in your bucket on GCS at "models/{timestamp}.h5" --> unit 02 only
    - if MODEL_TARGET='mlflow', also persist it on MLflow instead of GCS (for unit 0703 only) --> unit 03 only
    """
    if model == None:
        print("No model persisted")
        return None
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    # Save model locally
    model_path_folder = os.path.join(MODEL_LOCAL_REGISTRY_PATH, "models")
    create_folder_if_not_exist(model_path_folder)

    model_path = os.path.join(model_path_folder, f"{timestamp}.joblib")
    joblib.dump(model, model_path)
    print(":marca_de_verificação_branca: Model saved locally")
    if MODEL_TARGET == "gcs":
        # :presente: We give you this piece of code as a gift. Please read it carefully! Add a breakpoint if needed!
        model_filename = model_path.split("/")[-1] # e.g. "20230208-161047.h5" for instance
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(f"models/{model_filename}")
        blob.upload_from_filename(model_path)
        print(":marca_de_verificação_branca: Model saved to GCS")
        return None
    if MODEL_TARGET == "mlflow":
        mlflow.tensorflow.log_model(
            model=model,
            artifact_path="model",
            registered_model_name=MLFLOW_MODEL_NAME
        )
        print(":marca_de_verificação_branca: Model saved to MLflow")
        return None
    return None
def create_folder_if_not_exist(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
