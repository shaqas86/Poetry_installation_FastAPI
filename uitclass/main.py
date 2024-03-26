from contextlib import asynccontextmanager
from http import client
from  fastapi import FastAPI, HTTPException
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
# @app.put("/todos/{todo_id}")
# def update_todo(todo_id: int, todo: Todo):
#        with Session(engine) as session:
#               session.exec(Todo).filter(Todo.id == todo_id)
#               session.commit()
#               session.close()
#               return todo

@app.get("/todos/")
def read_todos():
       with Session(engine) as session:
              todos = session.exec((Todo)).all()
              return todos
       
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_update: Todo):
       with Session(engine) as session:
              todo=session.get(Todo, todo_id)
              if todo is None:
                     raise HTTPException(status_code=404, detail="Todo not found")
              if todo_update.content:
                     todo.content = todo_update.content
                     session.commit()
                     session.refresh(todo)
                     return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
       with Session(engine) as session:
              todo=session.get(Todo, todo_id)
              if todo is None:
                     raise HTTPException(status_code=404, detail="Todo not found")
              session.delete(todo)
              session.commit()
              return {"response":"todo deleted"}

