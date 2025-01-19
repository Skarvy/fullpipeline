# Usamos la imagen Jenkins LTS como base
FROM jenkins/jenkins:lts

# Copiamos el binario de Docker desde la imagen docker:cli
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin

# Cambiamos a usuario root para configurar permisos y herramientas
USER root

# Instalamos kubectl con verificación de checksum
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256" \
    && echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/kubectl \
    && rm kubectl.sha256 \
    && echo "kubectl instalado correctamente: $(kubectl version --client --short || echo 'Error en instalación')"

# Instalamos KIND con verificación de checksum
RUN curl -Lo ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.18.0/kind-linux-amd64 \
    && curl -Lo ./kind.sha256 https://github.com/kubernetes-sigs/kind/releases/download/v0.18.0/kind-linux-amd64.sha256 \
    && echo "$(cat kind.sha256)  ./kind" | sha256sum --check \
    && chmod +x ./kind \
    && mv ./kind /usr/local/bin/kind \
    && rm kind.sha256 \
    && echo "kind instalado correctamente: $(kind --version || echo 'Error en instalación')"

# Instalamos Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && echo "Docker Compose instalado correctamente: $(docker-compose --version || echo 'Error en instalación')"

# Creamos el grupo 'docker' y agregamos al usuario 'jenkins'
RUN groupadd docker && usermod -aG docker jenkins

# Configuramos permisos para el usuario Jenkins
RUN chown -R jenkins:jenkins /var/jenkins_home

# Volvemos al usuario Jenkins
USER jenkins

