from fastapi import FastAPI
from pyndantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os


load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]


class Annotation(BaseModel):
    user: str
    date: str
    layer: str
    type: str
    coordinates: list

@app.post("/annotations")
def create_annotation(annotation: Annotation):
    result = annotations_collection.insert_one(annotation.dict())
    return {"id": str(result.inserted_id)}


@app.get("/annotations")
def get_annotations(date: str = None, layer: str =None):
    query = {}
    if date:
        query["date"] = date
    if layer:
        query["layer"] = layer
    results = list(annotation_collection.find(query))
    for r in results:
        r["_id"] = str(r["_id"])
    return results

@app.delete("/annotations/{annotation_id}")
def delete_annotation(annotation_id: str):
    result = annotations_collection.delete_one({"_id" : ObjectId(annotation_id)})
    if result.deleted_count == 1:
        return { "message": "Deleted" }
    return { "message": "Not found" }