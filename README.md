# Django API Project

Este proyecto es una API desarrollada con Django, un framework web de alto nivel que permite el desarrollo rápido y limpio de aplicaciones web.

## Descripción

El objetivo de este proyecto es crear una API robusta y escalable utilizando Django. La API proporcionará varios endpoints para interactuar con los datos y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## Estructura del Proyecto

La estructura del proyecto sigue las convenciones estándar de Django:

- `manage.py`: Script de utilidad para interactuar con el proyecto Django.
- `project_name/`: Carpeta principal del proyecto que contiene configuraciones y aplicaciones.
  - `settings.py`: Configuraciones del proyecto.
  - `urls.py`: Definición de las rutas de la aplicación.
  - `wsgi.py`: Configuración para el servidor WSGI.
- `app_name/`: Carpeta de la aplicación Django que contiene modelos, vistas, y archivos de migración.

Además, este repositorio es un monorepo que contiene tanto el servidor (API) como el cliente. La estructura del cliente es la siguiente:

- `client/`: Carpeta que contiene el código del cliente.
  - `src/`: Código fuente del cliente.
  - `public/`: Archivos públicos del cliente.
  - `package.json`: Archivo de configuración del cliente.

## Instalación

Para configurar el entorno de desarrollo, sigue estos pasos:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea un entorno virtual e instálalo:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

4. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

Para configurar el cliente, sigue estos pasos adicionales:

1. Navega a la carpeta del cliente:
    ```bash
    cd client
    ```

2. Instala las dependencias del cliente:
    ```bash
    npm install
    ```

3. Inicia el servidor de desarrollo del cliente:
    ```bash
    npm start
    ```

## Uso

Una vez que el servidor esté en funcionamiento, puedes interactuar con la API utilizando herramientas como `curl`, `Postman` o cualquier cliente HTTP. Los endpoints disponibles se documentarán en una sección futura.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
