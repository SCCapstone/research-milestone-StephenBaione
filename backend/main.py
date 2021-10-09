import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.db.model.user import Base as UserBase
from src.db.database import SessionLocal, engine

# -------- Router Imports --------
from src.routes.authentication import authentication_router

# -------- Create database tables --------
UserBase.metadata.create_all(bind=engine)

app = FastAPI()

# -------- Origins --------
# White-list front end url
origins = [
    "http://localhost:8100",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# -------- Router Include --------
app.include_router(authentication_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
