# Usamos la imagen lts
# Usamos la imagen Jenkins LTS
FROM jenkins/jenkins:lts

# Copiamos el binario de Docker desde la imagen docker:dind
COPY --from=docker:dind /usr/local/bin/docker /usr/local/bin

# Cambiamos a usuario root para configurar permisos
USER root

# Creamos el grupo 'docker' y agregamos al usuario 'jenkins'
RUN groupadd docker && usermod -aG docker jenkins

# Volvemos al usuario Jenkins
USER jenkins
