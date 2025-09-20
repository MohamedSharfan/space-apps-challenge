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

