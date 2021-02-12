import uvicorn

from fastapi import FastAPI, Depends

from .views import router as views_router
from .auth import verify_client_key


app = FastAPI(title="Async API")

app.include_router(views_router, prefix='', dependencies=[Depends(verify_client_key)])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

