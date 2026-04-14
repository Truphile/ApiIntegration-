from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes.classify import router

app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_headers=["*"],
                   allow_methods=["*"],
                   allow_credentials=True)


@app.get("/")
async def root():
    return {"message": "OK"}

app.include_router(router, prefix="")


