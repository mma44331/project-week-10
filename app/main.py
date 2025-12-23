import uvicorn
from fastapi import FastAPI

app = FastAPI()




@app.get("/contacts")
def get_contacts():
    pass
@app.post("/contacts")
def create_new_contact():
    pass

@app.put("/contacts/{id}")
def update_contact(id:str):
    pass

app.delete("/contacts/{id}")
def delete_contact(id:str):
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",port=8000 , reload=True)
