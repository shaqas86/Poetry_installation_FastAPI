from  fastapi import FastAPI

app : FastAPI =FastAPI()

@app.get("/")
def getname():
        return {"response":"hello world"}