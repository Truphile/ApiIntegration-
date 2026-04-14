from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes.classify import router

app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
                   allow_headers=["*"],
                   allow_methods=["*"],
                   allow_credentials=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix="/api")


