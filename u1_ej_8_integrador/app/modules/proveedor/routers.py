from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import List, Optional
from . import schemas, services


# Router principal del módulo Proveedores
router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

@router.post(
    "/",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_201_CREATED,
)
def alta_proveedor(proveedor: schemas.ProveedorCreate):
    # Intentamos crear el proveedor
    nuevo = services.crear(proveedor)

    # Si el código ya existe, devolvemos conflicto
    if nuevo is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El código del proveedor ya existe",
        )

    return nuevo


@router.get(
    "/",
    response_model=List[schemas.ProveedorRead],
    status_code=status.HTTP_200_OK,
)
def listar_proveedores(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
    activo: Optional[bool] = Query(None),
):
    # Obtenemos los proveedores aplicando el filtro de estado
    proveedores = services.obtener_todas(skip, limit, activo)

    return proveedores


@router.get(
    "/{id}",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_200_OK,
)
def detalle_proveedor(id: int = Path(..., gt=0)):
    # Buscamos el proveedor por su ID
    proveedor = services.obtener_por_id(id)

    # Si no existe, devolvemos 404
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado",
        )

    return proveedor

@router.put(
    "/{id}",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_200_OK,
)
def actualizar_proveedor(
    proveedor: schemas.ProveedorCreate,
    id: int = Path(..., gt=0),
):
    # Intentamos actualizar el proveedor
    actualizado = services.actualizar_total(id, proveedor)

    # Si el ID no existe, devolvemos 404
    if actualizado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado",
        )

    # Si el código ya pertenece a otro proveedor, devolvemos 409
    if actualizado == "DUPLICADO":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El código del proveedor ya existe",
        )

    return actualizado


@router.put(
    "/{id}/desactivar",
    response_model=schemas.ProveedorRead,
    status_code=status.HTTP_200_OK,
)
def desactivar_proveedor(id: int = Path(..., gt=0)):
    # Intentamos desactivar el proveedor
    desactivado = services.desactivar(id)

    # Si el ID no existe, devolvemos 404
    if desactivado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado",
        )

    # Si el proveedor ya estaba desactivado, devolvemos 409
    if desactivado == "YA_DESACTIVADO":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El proveedor ya está desactivado",
        )

    return desactivado

