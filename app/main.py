from fastapi import FastAPI
from .routers import router as webhook_router


app = FastAPI()

app.include_router(webhook_router)
