from auth.routers import router as auth_router
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def get_health():
    return "ok"


app.include_router(auth_router, prefix="/auth")
