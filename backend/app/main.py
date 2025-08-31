from fastapi import FastAPI

app = FastAPI(title="Grocery Price Tracker")

@app.get("/")
def root():
    return {"message": "API is running 🚀"}
