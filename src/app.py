from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.requests import Request
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(gym_classes_router)
app.include_router(clients_router)
app.include_router(gym_passes_router)
