from fastapi import FastAPI,HTTPException
from initiators.db_init import db_init
from initiators.setRoutes import setRoutes
from initiators.init_data import init_base_data
from initiators.init_logger import create_logger, log_exception
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from initiators.init_env import load_env_var



baseApp = FastAPI(
    description="this is Samyar project",
    title="Samyar Project",
    version="0.1.0"
)

db_init()
init_base_data()
setRoutes(baseApp)
load_env_var()
logger = create_logger(baseApp)
baseApp.middleware("http")(log_exception)

origins = [
    "https://your-frontend-domain.com"
]

baseApp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["post","get","put","delete"],
    allow_headers=["*"],
)

@baseApp.middleware("http")
async def block_dissAlowed_origins(request, call_next):
    origin = request.headers.get("origin")
    if origin not in origins:
        return JSONResponse(status_code=403, content={"message": "Dissallowed origin"})
    else:
        response = await call_next(request)
        return response