from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ..init import templates
from ..lib.schemas.Item import Item, Base
from ..lib.models.Item import ItemModel
from app.lib.models.Item import SessionLocal
from sqlalchemy import engine

router = APIRouter()

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