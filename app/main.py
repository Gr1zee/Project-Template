from fastapi import FastAPI
from .routers.router import router
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


app = FastAPI()

app.include_router(router)