from fastapi import FastAPI
from initiators.db_init import db_init
from initiators.setRoutes import setRoutes


baseApp = FastAPI(
    description="this is Samyar project",
    title="Samyar Project",
    version="0.1.0"
)

db_init()
setRoutes(baseApp)