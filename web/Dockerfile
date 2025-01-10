# Usa una imagen base oficial de Node.js 18
FROM node:18-slim as build

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Copia el archivo .env al contenedor
COPY .env /app/.env

# Instala las dependencias
RUN npm install

# Construye la aplicación para producción
RUN npm run build

# Usa una imagen base ligera para servir el contenido
FROM nginx:stable-alpine

# Copia los archivos generados por el build al directorio de Nginx (cambiar build por dist)
COPY --from=build /app/dist /usr/share/nginx/html

# Expone el puerto donde se servirá la aplicación
EXPOSE 80

# Comando para iniciar Nginx
CMD ["nginx", "-g", "daemon off;"]
