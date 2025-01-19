pipeline {
    agent any
    environment {
        DOCKER_USERNAME = 'skardevops'
        FRONTEND_IMAGE = "${DOCKER_USERNAME}/frontend:latest"
        BACKEND_IMAGE = "${DOCKER_USERNAME}/backend:latest"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Skarvy/fullpipeline.git'
            }
        }
        stage('Build Docker Images') {
            steps {
                sh "docker build -t $BACKEND_IMAGE ./api"
                sh "docker build -t $FRONTEND_IMAGE ./web"
            }
        }
        stage('Push Docker Images to Registry') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh """
                    echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin
                    docker push $BACKEND_IMAGE
                    docker push $FRONTEND_IMAGE
                    """
                }
            }
        }
        stage('Deploy with Docker Compose') {
            steps {
                sh """
                docker-compose down || true
                docker-compose up -d --build
                """
            }
        }
        stage('Monitor and Validate') {
            steps {
                sh "docker ps"
            }
        }
    }
    post {
        always {
            sh "docker logout"
        }
    }
}
