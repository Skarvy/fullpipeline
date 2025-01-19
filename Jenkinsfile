pipeline {
    agent any
    stages {
        stage('Verify Docker Installation') {
            steps {
                script {
                    echo "Checking Docker installation..."
                    sh 'docker --version || exit 1' // Verifica si Docker está instalado
                    sh 'docker info || exit 1'     // Verifica si Docker está funcionando correctamente
                }
            }
        }
        stage('Verify Docker Compose Installation') {
            steps {
                script {
                    echo "Checking Docker Compose installation..."
                    sh 'docker-compose --version || exit 1' // Verifica si Docker Compose está instalado
                }
            }
        }
        stage('List Docker Data Directory') {
            steps {
                script {
                    echo "Listing Docker data directory..."
                    sh 'docker info | grep "Docker Root Dir" || exit 1' // Muestra la ubicación del directorio de datos de Docker
                }
            }
        }
    }
}
