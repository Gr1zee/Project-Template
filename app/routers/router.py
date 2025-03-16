from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ..init import templates
from ..lib.schemas.Item import Item
from sqlalchemy import engine
from sqlalchemy import create_engine, Column, Integer, String, Float, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


router = APIRouter()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class ItemModel(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)

Base.metadata.create_all(bind=engine)

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "World"})

@router.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("index.html", {"request": request, "name": name})

@router.post("/items/")
async def create_item(item: Item):
    db_item = ItemModel(**item.dict())
    db = SessionLocal()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

# Эндпоинт для получения всех элементов
@router.get("/items/")
async def get_items():
    db = SessionLocal()
    items = db.query(ItemModel).all()
    db.close()
    return items