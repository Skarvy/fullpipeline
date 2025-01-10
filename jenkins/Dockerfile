# Usamos la imagen lts
FROM jenkins/jenkins:lts

# Usamos la imagen docker:dind y copiamos el binario a /usr/local/bin
COPY --from=docker:dind /usr/local/bin/docker /usr/local/bin

# Cambiamos al usuario root para ejecutar comandos con permisos de superusuario
USER root

# Creamos el grupo docker si no existe y agregamos al usuario jenkins al grupo
RUN groupadd -g 999 docker && usermod -aG docker jenkins

# Volvemos al usuario jenkins
USER jenkins

