import time
from pinecone import Pinecone
from pinecone import ServerlessSpec
from openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pinecone.core.openapi.shared.exceptions import PineconeApiException

open_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

pantry_df = pd.read_csv('../data/pantry_mock_data.csv')
fridge_df = pd.read_csv('../data/fridge_mock_data.csv')
spice_df = pd.read_csv('../data/spice_mock_data.csv')

load_dotenv()
client = OpenAI(api_key=open_api_key)

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)

# Define a function to insert data into Pinecone
def insert_data(df, item_column, metadata_columns, namespace):
  for _, row in df.iterrows():
    item_name = row[item_column]
    embedding = get_openai_embedding(item_name)
    metadata = {col: row[col] for col in metadata_columns}
    index.upsert([(item_name, embedding, metadata)], namespace=namespace)

def get_openai_embedding(text):
  response = client.embeddings.create(model="text-embedding-3-small", input=[text])
  return response.data[0].embedding

# Create or connect to a single Pinecone index
index_name = "food-inventory"

try:
  if index_name not in pc.list_indexes():
    pc.create_index(
      name=index_name,
      dimension=1536,
      metric="cosine",
      spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
      )
    )
    print(f"Index '{index_name}' created.")
    # Wait for the index to be ready
    time.sleep(10)  # Adjust sleep time if necessary
    while index_name not in pc.list_indexes():
      print("Waiting for index to be ready...")
      time.sleep(5)

except PineconeApiException as e:
  if e.status == 409:
    print(f"Index '{index_name}' already exists.")
  else:
    raise

# Connect to the index
index = pc.Index(index_name)

# Insert data with appropriate namespaces
insert_data(pantry_df, "Item Name", ["Category", "Quantity", "Expiry Date", "Purchase Date", "Brand"], namespace="pantry")
insert_data(fridge_df, "Item Name", ["Type", "Quantity", "Expiry Date", "Storage Location"], namespace="fridge")
insert_data(spice_df, "Spice Name", ["Quantity", "Expiry Date", "Type"], namespace="spices")