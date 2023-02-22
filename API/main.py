from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from databases.database import Base, engine
from routers import (
    user_routes,
    post_routes,
    auth_routes,
)

app = FastAPI()

Base.metadata.create_all(engine)
# provide static access to /images
app.mount("/images", StaticFiles(directory="images"), "images")

app.include_router(user_routes.router)
app.include_router(post_routes.router)
app.include_router(auth_routes.router)


@app.get("/")
def root():
    return "You have reached the homepage"
