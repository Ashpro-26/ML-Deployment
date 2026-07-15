import os
import logging
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from joblib import dump

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report

load_dotenv()

def train_model():
    try:
        PROJECT_ROOT = Path(os.getenv("PROJECT_ROOT"))

        DATASET_PATH = PROJECT_ROOT / os.getenv("DATASET_NAME")
        MODEL_PATH = PROJECT_ROOT / os.getenv("MODEL_DIR") / os.getenv("MODEL_NAME")
        LOG_PATH = PROJECT_ROOT / os.getenv("LOG_DIR") / os.getenv("LOG_NAME")

        TARGET = os.getenv("TARGET")
        TEST_SIZE = float(os.getenv("TEST_SIZE"))
        RS = int(os.getenv("RS"))

        MODEL_PATH.parent.mkdir(parents= True,exist_ok= True)
        LOG_PATH.parent.mkdir(parents= True, exist_ok= True)

        print(DATASET_PATH)
        print(MODEL_PATH)

        logging.basicConfig(
            level= logging.INFO,
            format= "%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(LOG_PATH)
            ]
        )

        logging.info("Training Script Started")
        df = pd.read_csv(DATASET_PATH)
        logging.info(f"Dataset Loaded with the Shape:{df.shape}")

        X = df.drop(columns= [TARGET])
        y = df[TARGET]

        X_train,X_test,y_train,y_test = train_test_split(
            X, y, test_size= TEST_SIZE, random_state= RS, stratify= y
        )

        pipeline = Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("model", LogisticRegression(class_weight= "balanced"))
            ]
        )

        pipeline.fit(X_train, y_train)
        logging.info("Model Training Completed.")

        train_acc = accuracy_score(y_train, pipeline.predict(X_train))
        test_acc = accuracy_score(y_test, pipeline.predict(X_test))

        train_report = classification_report(y_train, pipeline.predict(X_train))
        test_report = classification_report(y_test, pipeline.predict(X_test))

        logging.info(f"Training Accuracy:{train_acc:.3f}")
        logging.info(f"Testing Accuracy:{test_acc:.3f}")

        logging.info(f"Train Classification Report \n {train_report}")
        logging.info(f"Test Classification Report \n {test_report}")

        dump(pipeline, MODEL_PATH)
        logging.info(f"Model saved to {MODEL_PATH}")

        logging.info("Training Script Finished")
    
    except Exception as e:
        print(f"Training Failed {e}")
        logging.exception(f"Training Script failed: {e}")
        raise


if __name__ == "__main__":
    train_model()