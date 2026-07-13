from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {
        "message": "Pokemon_Guide website is working"
    }