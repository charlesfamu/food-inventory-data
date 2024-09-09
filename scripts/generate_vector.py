from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

open_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=open_api_key)

def get_openai_embedding(text):
  response = client.embeddings.create(model="text-embedding-3-small", input=[text])
  return response.data[0].embedding

vector = get_openai_embedding("Pork Loin")

file_path = "embedding_vector.json"

with open(file_path, "w") as file:
    json.dump(vector, file)