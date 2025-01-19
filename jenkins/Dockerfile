# Usamos la imagen Jenkins LTS
FROM jenkins/jenkins:lts

# Copiamos el binario de Docker desde la imagen docker:dind
COPY --from=docker:dind /usr/local/bin/docker /usr/local/bin

# Cambiamos a usuario root para configurar permisos y herramientas
USER root
# Instalamos kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/kubectl \
    && echo "kubectl instalado correctamente: $(kubectl version --client --short || echo 'Error en instalación')"

# Instalamos KIND
RUN curl -Lo ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.18.0/kind-linux-amd64 \
    && chmod +x ./kind \
    && mv ./kind /usr/local/bin/kind \
    && echo "kind instalado correctamente: $(kind --version || echo 'Error en instalación')"

# Creamos el grupo 'docker' y agregamos al usuario 'jenkins'
RUN groupadd docker && usermod -aG docker jenkins

# Configuramos permisos para el usuario jenkins si fuera necesario
RUN chown -R jenkins:jenkins /var/jenkins_home

# Volvemos al usuario Jenkins
USER jenkins
