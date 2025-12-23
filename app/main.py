import uvicorn
from fastapi import FastAPI
from data_interactor import Connect
from pydantic import BaseModel


class contact(BaseModel):
    first_name:str | None = None
    last_name:str | None = None
    phone_number:str | None = None




app = FastAPI()


con = Connect()


@app.get("/contacts")
def get_all_contacts():
    data = con.get_contacts()
    return data

@app.post("/contacts")
def create_new_contact(contact:contact):
    return con.create_new_contact(contact)

@app.put("/contacts/{id}")
def update_contact(id:str,contact:contact):
    return con.updeta_contact(id,contact)

@app.delete("/contacts/{id}")
def delete_contact(id:str):
    return con.delete_contact(id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",port=8000 , reload=True)
