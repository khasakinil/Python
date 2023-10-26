from fastapi import FastAPI

app = FastAPI()

@app.get("/first-api")
async def first_api():
    return {"message" : "Hello, Good morning!!!"}