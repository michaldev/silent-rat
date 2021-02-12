import uvicorn
from fastapi import FastAPI, Depends

from src.communication import initialized_communication
from .auth import verify_client_key
from .views import router as views_router

app = FastAPI(title="Async API")

app.include_router(views_router, prefix='',
                   dependencies=[Depends(verify_client_key)])


@app.on_event("startup")
async def startup():
    await initialized_communication.initialize()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
