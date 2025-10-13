# Primer prueba de FastAPI

## Para que sirve FastAPI?

FastAPI es un framework web moderno y rápido para construir APIs con Python 3.7+ basado en las anotaciones de tipos estándar de Python. Algunas de sus características principales incluyen:
- **Alto rendimiento**: FastAPI es uno de los frameworks web más rápidos disponibles, comparable a Node.js y Go.
- **Fácil de usar**: Su diseño intuitivo facilita la creación y el mantenimiento de aplicaciones web.
- **Validación automática**: Utiliza Pydantic para la validación de datos, lo que garantiza que los datos de entrada sean correctos.
- **Documentación automática**: Genera documentación interactiva de la API automáticamente utilizando Swagger UI y ReDoc.


## Instalar las dependencias con uv
Nota: para mayor comodidad abre code en la carpeta reunion_8

```bash
pip install uv
```

Luego para crear el entorno virtual y agregar las dependencias

```bash
uv init
uv venv # Si usas VSCode seleccionar el entorno virtual creado
uv add "fastapi[standard]"
```

### Para usuarios de Pycharm

Si usas Pycharm, crea un entorno virtual desde la interfaz de Pycharm y luego instala las dependencias con pip.

## Crear main.py

Vamos a usar el ejemplo "Hello World" de FastAPI.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## El ejecutable de FastAPI

Pruebe `fastapi -h` para ver las opciones que ofrece.

Para correr el programa ejecute

```bash
fastapi dev main.py
```

Cuando haga cambios en el codigo watchman automaticamente reinicia el programa.


## Bruno como herramienta de prueba de API

Instala bruno desde [aquí](https://www.usebruno.com/)
