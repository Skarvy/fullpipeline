pipeline {
    agent any
    stages {
        stage('Checkout Repo') {
            steps {
                script {
                    echo "Cloning the repository..."
                    git branch: 'main', url: 'https://github.com/Skarvy/fullpipeline.git'
                }
            }
        }
        stage('Verify Docker Installation') {
            steps {
                script {
                    echo "Checking Docker installation..."
                    sh 'docker --version || exit 1'
                    sh 'docker info || exit 1'
                }
            }
        }
        stage('Verify Docker Compose Installation') {
            steps {
                script {
                    echo "Checking Docker Compose installation..."
                    sh 'docker-compose --version || exit 1'
                }
            }
        }
        stage('Stop and Remove Existing Containers') {
            steps {
                script {
                    echo "Stopping and removing existing containers..."
                    sh 'docker-compose down || exit 1'  // Detiene y elimina los contenedores previos
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    echo "Building Docker images..."
                    sh 'docker-compose build || exit 1'  // Fuerza la construcción de las imágenes
                }
            }
        }
        stage('Run Docker Compose Up') {
            steps {
                script {
                    echo "Starting Docker Compose..."
                    sh 'docker-compose up -d || exit 1'  // Levanta los contenedores en segundo plano
                }
            }
        }
        stage('List Docker Data Directory') {
            steps {
                script {
                    echo "Listing Docker data directory..."
                    sh 'docker info | grep "Docker Root Dir" || exit 1'
                }
            }
        }
    }
}
