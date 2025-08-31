# 1-Gestor-de-descargas
Este proyecto sera uno más de mis proyectos para mi portafolio de proyectos. Cualquier tipo de persona que pueda ver mi repositorio tiene la libertad de mi proyectos
sin ninguna restriccion alguna.

# Estructura del proyecto
``` bash
├── README.md
├── __pycache__
│   └── config.cpython-313.pyc
├── config.py
└── main.py
```
---
# Funcionamiento de cada código
- **`main.py`**: Es la parte lógica en donde se maneja todo la lógica del proyecto.
- **`config.py`**: Es la parte de configuración de la app.
---
# Funcionamiento del proyecto
Primero para poder usar el proyecto, pprimero se tiene que dirigir al archivo `config.py` en donde se encuentra la primera configuración de rutas:
```python
# Rutas base
ruta_descargas = "/Users/cristopherrobledo/Downloads/"
ruta_de_organizacion = "/usr/cristopherrobledo/Documentos"
```
- Tenemos una variable `ruta_descargas` en donde se tiene que colocar la ruta de las Descargas del archivo.
- La variable `ruta_de_organizacion` sirve para indicar la creacion de la carpeta padre donde se organizan los archivos organizados.

El segundo paso seria paso seria crear las categorias y las extensiones necesarias para crear carpetas de organizacion.
Su estructura es la siguiente:
```python
# Categoriasa y extensiones
categorias = {
    "<categoria>": ["<extension1>", "<extension2>", ...],
    "<categoria>": ["<extension1>", "<extension2>", ...], 
    "...": "..."
```
NOTA IMPORTANTE: Se tiene que respestar el nombre del diccionario y la lista.
Y listo, a probar!
