## Proyecto Final de Bootcamp DevOps: Avatares 🚀

### Descripción del Proyecto:
Avatares es un proyecto de muestra diseñado para demostrar el uso de contenedores en un entorno DevOps. Consiste en un backend de API web en Python 3.10 para generar avatares y un frontend de SPA (aplicación de página única) en Node.js 18. El objetivo de este proyecto es aplicar prácticas y herramientas de DevOps para mejorar la calidad, rendimiento, seguridad y eficiencia operativa de la aplicación.

![](./docs/2.png)

Más Información: [Enlace](./ABOUT.md)

## Arquitectura
![](./docs/3.png)

## Funcionamiento

![](./docs/4.png)

#### Componentes del Proyecto:
1. **Backend de API (Python 3.10):**
   - El backend de la API está desarrollado en Python 3.10 utilizando un framework web como Flask.
   - carpeta /api
   - Codigo principal app.py
   - Requiere dos variables de entorno
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   ```
   - La API proporciona endpoints para generar avatares basados en diferentes parámetros de entrada.
   - Metodos GET:
   ```
   /api/avatar
   /api/avatar/spec
   /ready
   ```

2. **Frontend SPA (Node.js 18):**
   - El frontend es una aplicación de página única (SPA) desarrollada en Node.js 18 utilizando un framework como React+vite.
   - Carpeta web/
   - Requiere dos variables de entorno
    ```
    VITE_HOST=0.0.0.0
    VITE_PORT=5173
    ```
   - Usar el gestor de paquetes npm
   - El frontend se comunica con el backend a través de solicitudes HTTP para generar y mostrar avatares.


 ## Despliegue con Docker y Jenkins



El proyecto está configurado para ejecutarse en contenedores Docker utilizando Docker Compose. La integración con Jenkins permite automatizar el flujo de desarrollo y despliegue continuo.

Configuración de Docker Compose

El archivo docker-compose.yml define los servicios necesarios:

**Frontend:**

Construcción desde ./web con la imagen de Node.js.

Exposición en el puerto 3001.

Comunicación con el backend mediante la variable de entorno REACT_APP_API_URL.

**Backend:**

Construcción desde ./api con Flask.

Exposición en el puerto 5000.


## Pipeline de Jenkins


**El pipeline automatiza las siguientes tareas:**

Clonación del repositorio.

Verificación de la instalación de Docker y Docker Compose.

Eliminación de contenedores existentes.

Construcción de imágenes Docker.

Levantamiento de los servicios.

Inspección del entorno de Docker.

Este flujo garantiza un despliegue confiable y reproducible de la aplicación.