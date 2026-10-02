from typing import List, Optional

from sqlmodel import Session
from fastapi import HTTPException, status

from .schemas import ProductoCreate
from .models import Producto
from . import repository


def crear(
    session: Session,
    data: ProductoCreate
) -> Producto:
    producto_existente = repository.obtener_por_nombre(session, data.nombre)

    if producto_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un producto con ese nombre"
        )

    nuevo_producto = Producto(**data.model_dump())

    return repository.crear(session, nuevo_producto)



def obtener_todos(
    session: Session,
    skip: int,
    limit: int
) -> List[Producto]:
    return repository.obtener_todos(session, skip, limit)


def obtener_por_id(
    session: Session,
    id: int
) -> Optional[Producto]:
    return repository.obtener_por_id(session, id)


def actualizar_total(
    session: Session,
    id: int,
    data: ProductoCreate
) -> Optional[Producto]:
    producto = repository.obtener_por_id(session, id)

    if not producto:
        return None

    producto_existente = repository.obtener_por_nombre(session, data.nombre)

    if producto_existente and producto_existente.id != id:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un producto con ese nombre"
        )

    producto.sqlmodel_update(data.model_dump())

    return repository.actualizar(session, producto)



def desactivar(
    session: Session,
    id: int
) -> Optional[Producto]:
    producto = repository.obtener_por_id(session, id)

    if not producto:
        return None

    return repository.desactivar(session, producto)

def eliminar(
    session: Session,
    id: int
) -> Optional[Producto]:
    producto = repository.obtener_por_id(session, id)

    if not producto:
        return None

    repository.eliminar(session, producto)

    return producto


def obtener_estado_stock(
    session: Session,
    id: int
) -> Optional[dict]:
    producto = repository.obtener_por_id(session, id)

    if not producto:
        return None

    # Regla de negocio: determinar si el stock está por debajo del mínimo
    alerta_stock = producto.stock < producto.stock_minimo

    return {
        "stock": producto.stock,
        "bajo_stock_minimo": alerta_stock,
        "activo": producto.activo,
    }
