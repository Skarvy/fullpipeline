# Usamos la imagen Jenkins LTS como base
FROM jenkins/jenkins:lts

# Copiamos el binario de Docker desde la imagen docker:dind
COPY --from=docker:dind /usr/local/bin/docker /usr/local/bin

# Cambiamos a usuario root para configurar permisos y herramientas
USER root

# Instalamos Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && chown root:root /usr/local/bin/docker-compose \
    && chmod 755 /usr/local/bin/docker-compose \
    && echo "Docker Compose instalado correctamente: $(docker-compose --version || echo 'Error en instalación')"

# Agregamos al usuario jenkins al grupo root (no recomendado)
RUN usermod -aG root jenkins

# Agregamos al usuario jenkins al grupo docker (mejor opción)
RUN groupadd docker && usermod -aG docker jenkins

# Otorgamos permisos adecuados al socket de Docker
RUN chmod 666 /var/run/docker.sock

# Volvemos al usuario Jenkins
USER jenkins

