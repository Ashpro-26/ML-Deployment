import os
import logging
import pandas as pd
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

DATASET_PATH = os.getenv("DATASET_PATH")

logging.info("Loading Dataset")
df = pd.read_csv(DATASET_PATH)
logging.info("Dataset Loaded Successfully")

print(DATASET_PATH)
print(os.path.exists(DATASET_PATH))

print(df.head())