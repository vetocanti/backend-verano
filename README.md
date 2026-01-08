# Backend Verano

Proyecto Django para una tienda simple con listado de productos y categorías.

## Características

- Modelos: `Categoria`, `Producto`, `DetalleProducto`.
- Vista: `lista_productos` renderiza la plantilla `tienda/lista_productos.html`.
- Rutas principales:
  - `/productos/`: Lista los productos con su categoría y detalles.
  - `/admin/`: Panel de administración de Django.
- Base de datos: SQLite (`db.sqlite3`).

## Requisitos

- Python 3.10+ (recomendado)
- Django 6.0.1
- Windows (probado)

## Estructura del proyecto

```
backend-verano/
├─ manage.py
├─ db.sqlite3
├─ config/
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ asgi.py
│  └─ __init__.py
└─ tienda/
   ├─ models.py
   ├─ views.py
   ├─ urls.py
   ├─ templates/
   │  └─ tienda/
   │     └─ lista_productos.html
   └─ admin.py
```

## Puesta en marcha (Windows PowerShell)

1. Crear y activar entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
python -m pip install --upgrade pip
pip install django==6.0.1
```

3. Aplicar migraciones:

```powershell
python manage.py makemigrations
python manage.py migrate
```

4. (Opcional) Crear superusuario para el admin:

```powershell
python manage.py createsuperuser
```

5. Ejecutar el servidor de desarrollo:

```powershell
python manage.py runserver
```

6. Abrir en el navegador:

- Productos: http://127.0.0.1:8000/productos/
- Admin: http://127.0.0.1:8000/admin/

## Modelos

- `Categoria`: nombre.
- `Producto`: nombre, precio (entero), relación con `Categoria`.
- `DetalleProducto`: pares clave/valor asociados a `Producto`.

## Desarrollo

- Las plantillas viven en `tienda/templates/tienda/`.
- Añade más vistas y URLs en `tienda/views.py` y `tienda/urls.py`.
- Configura apps y middlewares en `config/settings.py`.

## Configuración

Valores relevantes en `config/settings.py`:

- `SECRET_KEY`: Mantener secreto en producción.
- `DEBUG`: Desactivar en producción.
- `ALLOWED_HOSTS`: Configurar dominios permitidos (p. ej. `["localhost", "127.0.0.1"]`).
- `DATABASES`: Por defecto SQLite; adapta para PostgreSQL/MySQL según necesidades.

Ejemplo rápido para producción (editar `config/settings.py` o usar variables de entorno):

```python
DEBUG = False
ALLOWED_HOSTS = ["mi-dominio.com"]
```

## Pruebas

Ejecutar tests de la app `tienda`:

```powershell
python manage.py test tienda
```

## Contribución

- Crea una rama y abre un Pull Request.
- Sigue el estilo del proyecto y añade pruebas cuando corresponda.

## Notas

- Proyecto generado con Django 6.0.1; el ajuste estándar usa SQLite.
- Para despliegue, considera configurar `STATIC_URL`, `STATIC_ROOT` y una base de datos de producción.
