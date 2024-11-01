from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI Proxy Service for Paystack and Apache Fineract"}