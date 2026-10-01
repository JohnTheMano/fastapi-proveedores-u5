from typing import List, Optional
from .schemas import ProveedorCreate, ProveedorRead

# Simulamos una base de datos en memoria
db_proveedores: List[ProveedorRead] = []

# Contador para generar IDs automáticamente
id_counter = 1


def crear(data: ProveedorCreate) -> ProveedorRead:
    global id_counter

    # Verificamos que el código del proveedor no esté repetido
    for proveedor in db_proveedores:
        if proveedor.codigo == data.codigo:
            return None

    # Creamos el nuevo proveedor con un ID único
    nuevo = ProveedorRead(id=id_counter, **data.model_dump())

    # Guardamos el proveedor en la lista
    db_proveedores.append(nuevo)

    # Incrementamos el contador para el próximo proveedor
    id_counter += 1

    return nuevo


def obtener_todas(
    skip: int = 0,
    limit: int = 10,
    activo: Optional[bool] = None,
) -> List[ProveedorRead]:

    # Filtramos por estado si se indicó activo
    proveedores = db_proveedores

    if activo is not None:
        proveedores = [
            proveedor
            for proveedor in proveedores
            if proveedor.activo == activo
        ]

    # Aplicamos la paginación sobre el resultado filtrado
    return proveedores[skip : skip + limit]



def obtener_por_id(id: int) -> Optional[ProveedorRead]:
    # Buscamos el proveedor por su ID
    for proveedor in db_proveedores:
        if proveedor.id == id:
            return proveedor

    # Si no existe, devolvemos None
    return None


def actualizar_total(
    id: int, data: ProveedorCreate
) -> Optional[ProveedorRead | str]:

    # Primero verificamos que el proveedor exista
    proveedor = obtener_por_id(id)

    if proveedor is None:
        return None

    # Verificamos que el nuevo código no pertenezca a otro proveedor
    for otro in db_proveedores:
        if otro.codigo == data.codigo and otro.id != id:
            return "DUPLICADO"

    # Creamos el proveedor actualizado manteniendo su ID
    actualizado = ProveedorRead(
        id=id,
        **data.model_dump()
    )

    # Reemplazamos el registro anterior
    for index, otro in enumerate(db_proveedores):
        if otro.id == id:
            db_proveedores[index] = actualizado
            return actualizado

    return None


def desactivar(id: int) -> Optional[ProveedorRead | str]:
    # Buscamos el proveedor por su ID
    proveedor = obtener_por_id(id)

    # Si el ID no existe, devolvemos None
    if proveedor is None:
        return None

    # Si ya estaba desactivado, devolvemos un indicador de conflicto
    if not proveedor.activo:
        return "YA_DESACTIVADO"

    # Creamos una copia con activo=False
    datos = proveedor.model_dump()
    datos["activo"] = False

    actualizado = ProveedorRead(**datos)

    # Reemplazamos el registro en la lista
    for index, otro in enumerate(db_proveedores):
        if otro.id == id:
            db_proveedores[index] = actualizado
            return actualizado

    return None
