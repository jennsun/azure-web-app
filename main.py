from azure.storage.blob import BlobServiceClient
from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

# Configure Azure
azure_connection_string = os.environ.get("AZURE_BLOB_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(azure_connection_string)
INPUT_CONTAINER = "original-videos"
OUTPUT_CONTAINER = "processed-videos"


@app.get("/test/")
def read_root():
    """Simple hello world test"""
    return {"Hello": "World"}


@app.get("/test2/{value}")
def manipulate_value(value):
    """Add 1 to the given parameter"""
    one_more = int(value) + 1
    return {"val": one_more}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Through the FastAPI endpoint, a user uploads a video. This video is saved to Azure Blob Storage in INPUT_CONTAINER. After the upload is complete, FastAPI triggers an Azure Batch job, sending it the location of the uploaded video in Blob Storage."""
    blob_client = blob_service_client.get_blob_client(
        container=INPUT_CONTAINER, blob=file.filename
    )
    print(f"blob client:{blob_client}")
    blob_client.upload_blob(file.file.read())
    # Here, you'd trigger the Azure Batch job for processing, passing the filename as a parameter
    return {"filename": file.filename}


@app.get("/processed/{filename}")
async def get_processed_video(filename: str):
    """Once processing is complete, FastAPI can serve the processed video back to the user, fetching it from the OUTPUT_CONTAINER in Azure Blob Storage."""
    # Logic to fetch the processed video from Azure Blob and return to the user
    pass
