import os
from dotenv import load_dotenv

#Load env files from environment variables
load_dotenv()

dataset_path = os.getenv("DATASET_PATH")
model_path = os.getenv("MODEL_PATH")
environment = os.getenv("ENVIRONMENT")

print("Dataset Path:",dataset_path)
print("Model Path:",model_path)
print("Environment:",environment)