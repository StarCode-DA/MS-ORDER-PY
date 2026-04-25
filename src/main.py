from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.orders import router as orders_router

app = FastAPI(title="MS ORDER", redirect_slashes=False)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders_router)