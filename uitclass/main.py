from contextlib import asynccontextmanager
from  fastapi import FastAPI
from sqlmodel import SQLModel,Field,create_engine,Session,select
from typing import Union, Optional, Annotated
from uitclass import settings


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)

connection_string = str(settings.DATABASE_URL).replace("postgresql","postgresql+psycopg")

engine= create_engine(connection_string)

def creat_db_and_tables():
        Todo.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
       print("creating tables...")
       creat_db_and_tables()
       yield

def get_session():
       with get_session(engine) as session:
              yield session
app : FastAPI =FastAPI(lifespan=lifespan)

@app.get("/")
def getname():
        return {"response":"hello world"}

@app.get("/city")
def read_city():
        return {"city" :"Lahore"}

@app.get("/teacher")
def read_teacher():
        return{"teacher":"sir Qasim"}

@app.post("/todos/")
def create_todo(todo: Todo):
       with Session(engine) as session:
              session.add(todo)
              session.commit()
              session.refresh(todo)
              return todo

@app.get("/todos/")
def read_todos():
       with Session(engine) as session:
              todos = session.exec((Todo)).all()
              return todos

@app.post("/todos1/")
def create_todo(todo1: Todo):
       with Session(engine) as session:
              session.add(todo1)
              session.commit()
              session.refresh(todo1)
              return todo1