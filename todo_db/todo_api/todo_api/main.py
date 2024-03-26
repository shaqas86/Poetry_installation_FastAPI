from fastapi  import FastAPI
from typing import Union,Optional
from contextlib import asynccontextmanager
from todo_api import settings
from sqlmodel import Field,Session,SQLModel,create_engine,select

class Todo(SQLModel,table=True):
    id:int =Field(default=None,primary_key=True)
    title:str =Field(index=True)

connection_string=str(settings.DATABASE_URL).replace(
    "postgresql","postgresql+psycopg")

engine=create_engine(connection_string,
                     connect_args={"sslmode":"require"},pool_recycle=300)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app :FastAPI):
    print("creating tables..")
    create_db_and_tables()
    yield

app= FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/todos")
def create_todo(todo:Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo
    
@app.get("/todos/")
def read_todos():
    with Session(engine) as session:
        todos=session.exec(select(Todo)).all()
        return todos

# app=FastAPI()
# @app.get("/")
# def home():
#     return {"message":"Welcome to Home Page"}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}