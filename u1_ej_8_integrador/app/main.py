from fastapi import FastAPI
from app.database import create_db_and_tables

from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router
from app.modules.proveedor.routers import router as proveedor_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Integradora - Unidad 1",
        description="Conceptos: Path, Query, Body, Pydantic, Errores.",
        version="1.0.0"
    )
    create_db_and_tables()

    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(proveedor_router)

    
    return app

app = create_app()
