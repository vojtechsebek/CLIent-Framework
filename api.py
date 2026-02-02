from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

token = "test"

@app.get("/setup/token")
async def get_setup_token():
    return {"token": token}