# Persistencia de Datos

En esta clase vamos a dotar a nuestros objetos de persistencia, es decir vamos a volcar el estado de los mismos en una base de datos para que no se pierdan al finalizar la ejecución del programa.


# Inicializacion

Recuerden abrir la carpeta reunion_10 directamente en visual studio code.

Una vez abierta la carpeta, abrir una terminal integrada y ejecutar:

```bash
uv venv
source venv/bin/activate
uv sync
```


# Requerimientos

- Docker
- Docker Compose

Instalar Docker desde [aquí](https://docs.docker.com/get-docker/).
Instalar Docker Compose desde [aquí](https://docs.docker.com/compose/install/).

# Configuración de MongoDB con Docker

Ejecutar el docker compose para levantar un contenedor con MongoDB:

```bash
docker-compose up -d
```

# Inspeccion de la base de datos

Podemos inspeccionar la base de datos utilizando MongoDB Compass, una herramienta gráfica para interactuar con MongoDB.
Descargar MongoDB Compass desde [aquí](https://www.mongodb.com/docs/compass/install/).

# Conexión a MongoDB

Abrir MongoDB Compass e ingresar la siguiente cadena de conexión:

```
mongodb://root:example@localhost:27017
```

# Novedades en el código

## Infraestructura de base de datos

Se integró MongoDB al proyecto creando una nueva clase DatabaseConnection en internal/database.py. Esta conexión se inicializa en main.py y se propaga a través de las capas de la aplicación (Router → Repository → Service).

## Modelos y esquemas

Se añadió el archivo schemas.py con tres esquemas Pydantic (para FastAPI) para validar las operaciones: creación, detalle y actualización de productos.

Se añadio en schemas.py los esquemas para serializar y deserializar los productos para la base de datos MongoDB.

## Feature: Actualización de productos
Se implementó el flujo completo end-to-end para actualizar y eliminar productos:
- Router (app/products/router.py): Rutas de actualización y eliminación de productos
- Service (app/products/service.py): Lógica de negocio del update y delete
- Repository (app/products/repository.py): Persistencia en MongoDB
- Router, Repository, Service: Todos ahora aceptan y usan la conexión a BD
