#importing the necesssary requirements
from fastapi import FastAPI
from .setup_main import configure_cors
from contextlib import asynccontextmanager
from .database_setup import init_db, engine

#importing the router
from .routers import color_analysis, binary_convert, fibonnacci_sum, recursive_search

#on event start up and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    try:
        yield
    finally:
        print("Application Shutdown: Cleanup complete.")

#fastapi instance
app = FastAPI(title="Bincom Staff T-Shirt Color Analysis",
    description="FastAPI service for the staff assessment covering data analysis, database simulation, and algorithms.",
    lifespan=lifespan
    )

#CORS middleware
configure_cors(app)

#including the route
app.include_router(color_analysis.router)
app.include_router(binary_convert.router)
app.include_router(fibonnacci_sum.router)
app.include_router(recursive_search.router)