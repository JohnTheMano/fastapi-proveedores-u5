from typing import List, Optional

from sqlmodel import Session, select

from .models import Producto


def crear(session: Session, producto: Producto) -> Producto:
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def obtener_todos(
    session: Session,
    skip: int,
    limit: int
) -> List[Producto]:
    return session.exec(
        select(Producto)
        .offset(skip)
        .limit(limit)
    ).all()


def obtener_por_id(
    session: Session,
    id: int
) -> Optional[Producto]:
    return session.get(Producto, id)

def obtener_por_nombre(
    session: Session,
    nombre: str
) -> Optional[Producto]:
    return session.exec(
        select(Producto).where(Producto.nombre == nombre)
    ).first()

def actualizar(
    session: Session,
    producto: Producto
) -> Producto:
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto

def eliminar(
    session: Session,
    producto: Producto
) -> None:
    session.delete(producto)
    session.commit()

def desactivar(
    session: Session,
    producto: Producto
) -> Producto:
    producto.activo = False

    session.add(producto)
    session.commit()
    session.refresh(producto)

    return producto
