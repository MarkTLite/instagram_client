from fastapi import FastAPI

from databases.database import Base, engine
from routers import user_routes

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(user_routes.router)

@app.get('/')
def root():
    return "Hello World"