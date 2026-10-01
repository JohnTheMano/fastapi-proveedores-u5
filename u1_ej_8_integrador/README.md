Trabajo Práctico 4 - Programación IV
API de Gestión de Proveedores

Este proyecto extiende la API REST de gestión de catálogo agregando el módulo Proveedores al proyecto base u1_ej_8_integrador.

El módulo permite:

Crear proveedores.
Listar proveedores.
Consultar un proveedor por ID.
Actualizar proveedores mediante reemplazo total.
Desactivar proveedores mediante borrado lógico.
Filtrar proveedores por estado.
Aplicar paginación mediante skip y limit.
Tecnologías
Python
FastAPI
Pydantic
REST Client
Estructura del módulo
app/
└── modules/
    └── proveedor/
        ├── __init__.py
        ├── routers.py
        ├── schemas.py
        └── services.py

Ejecución

Desde la carpeta u1_ej_8_integrador, instalar las dependencias:

pip install -r requirements.txt


Luego ejecutar el servidor:

fastapi dev app/main.py


La documentación interactiva de Swagger estará disponible en:

http://127.0.0.1:8000/docs

Pruebas

Los casos de prueba se encuentran en:

tests/test_api.http


Las pruebas incluyen casos exitosos y escenarios de error 404, 409 y 422.

Almacenamiento

Los datos de proveedores se almacenan en memoria mediante una lista de Python. No se utiliza una base de datos externa ni persistencia permanente.