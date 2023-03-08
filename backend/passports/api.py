# backend/passports/api.py
from fastapi import APIRouter
from pydantic import BaseModel
from firebase_admin import credentials, initialize_app, firestore

app = initialize_app()
db = firestore.client()

passports = APIRouter()


class Passport(BaseModel):
    id: str
    name: str
    country: str
    expiration_date: str


@passports.get("/passports")
async def read_passports():
    print("Reading passports...")
    passports = db.collection("passports").stream()
    return [passport.to_dict() for passport in passports]


@passports.post("/passports")
async def create_passport(passport: Passport):
    db.collection("passports").add(passport.dict())
    return passport


@passports.put("/passports/{id}")
async def update_passport(id: str, passport: Passport):
    db.collection("passports").document(id).set(passport.dict())
    return passport


@passports.delete("/passports/{id}")
async def delete_passport(id: str):
    db.collection("passports").document(id).delete()
    return {"message": "Passport deleted successfully."}
