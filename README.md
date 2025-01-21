Proyecto Final de Bootcamp DevOps: Avatares 🚀

Descripción del Proyecto:

Avatares es un proyecto de muestra diseñado para demostrar el uso de contenedores en un entorno DevOps. Consiste en un backend de API web en Python 3.10 para generar avatares y un frontend de SPA (aplicación de página única) en Node.js 18. El objetivo de este proyecto es aplicar prácticas y herramientas de DevOps para mejorar la calidad, rendimiento, seguridad y eficiencia operativa de la aplicación.

Más Información: Enlace

Arquitectura

El proyecto utiliza una arquitectura basada en contenedores mediante Docker y Docker Compose, asegurando una fácil implementación y escalabilidad. Se compone de dos servicios principales:

Backend: Desarrollado en Python 3.10 utilizando Flask.

Frontend: Construido con React+Vite sobre Node.js 18.

Ambos servicios se comunican a través de una red interna definida en Docker Compose.

Funcionamiento

El despliegue de la aplicación se realiza mediante un pipeline de Jenkins que automatiza el proceso de construcción, despliegue y verificación de los contenedores.

Componentes del Proyecto:

Backend de API (Python 3.10):

Carpeta: /api

Código principal: app.py

Variables de entorno requeridas:

FLASK_APP=app.py
FLASK_ENV=development

Endpoints disponibles:

GET /api/avatar
GET /api/avatar/spec
GET /ready

Frontend SPA (Node.js 18):

Carpeta: web/

Variables de entorno requeridas:

VITE_HOST=0.0.0.0
VITE_PORT=5173

Administrado con npm para la gestión de dependencias.

Despliegue con Docker y Jenkins

El proyecto está configurado para ejecutarse en contenedores Docker utilizando Docker Compose. La integración con Jenkins permite automatizar el flujo de desarrollo y despliegue continuo.

Configuración de Docker Compose

El archivo docker-compose.yml define los servicios necesarios:

Frontend:

Construcción desde ./web con la imagen de Node.js.

Exposición en el puerto 3001.

Comunicación con el backend mediante la variable de entorno REACT_APP_API_URL.

Backend:

Construcción desde ./api con Flask.

Exposición en el puerto 5000.

Pipeline de Jenkins

El pipeline automatiza las siguientes tareas:

Clonación del repositorio.

Verificación de la instalación de Docker y Docker Compose.

Eliminación de contenedores existentes.

Construcción de imágenes Docker.

Levantamiento de los servicios.

Inspección del entorno de Docker.

Este flujo garantiza un despliegue confiable y reproducible de la aplicación.