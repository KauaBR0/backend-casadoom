from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.product_routes import router as product_router
from database.config import MongoDB

app = FastAPI(
    title="API",
    description="API REST",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    await MongoDB.connect_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    await MongoDB.close_db()

app.include_router(product_router)

@app.get("/")
async def root():
    return {"message": "API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)