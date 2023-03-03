from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from databases.database import Base, engine
from routers import (
    user_routes,
    post_routes,
    auth_routes,
    comment_routes,
)

app = FastAPI()

# database
Base.metadata.create_all(engine)

# provide static access to /images
app.mount("/images", StaticFiles(directory="images"), "images")

# routers
app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(post_routes.router)
app.include_router(comment_routes.router)

# CORS policy
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)


@app.get("/")
def root():
    return "You have reached the homepage"
