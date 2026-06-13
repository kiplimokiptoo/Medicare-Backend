from fastapi import FastAPI

app = FastAPI(title="Medicare App API", version="0.1.0")


@app.get("/", tags=["root"])
async def read_root():
    return {"app": "Medicare App", "message": "Welcome to Medicare App API"}


@app.get("/api/v1/info", tags=["info"])
async def info():
    return {
        "name": "Medicare App",
        "services": ["Emergency", "Outpatient", "Inpatient"],
    }
