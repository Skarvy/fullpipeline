# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia todos los archivos de la aplicación al contenedor
COPY . /app
COPY tilt_shirt.svg .
COPY docker_shirt.svg .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Establece las variables de entorno necesarias para Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expone el puerto en el que Flask escuchará (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
