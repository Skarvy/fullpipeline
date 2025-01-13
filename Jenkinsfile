pipeline {
    agent any
    environment {
        K8S_NAMESPACE = 'mi-proyecto'
        DOCKER_USERNAME = 'skardevops' // Tu usuario en Docker Hub
        FRONTEND_IMAGE = "${DOCKER_USERNAME}/frontend:latest"
        BACKEND_IMAGE = "${DOCKER_USERNAME}/backend:latest"
        GRAFANA_IMAGE = 'grafana/grafana:latest'
        PROMETHEUS_IMAGE = 'prom/prometheus:latest'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Skarvy/fullpipeline.git'
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    sh "docker build -t $BACKEND_IMAGE ./api"
                    sh "docker build -t $FRONTEND_IMAGE ./web"
                }
            }
        }
        stage('Push Docker Images to Registry') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh """
                        echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin
                        docker push $BACKEND_IMAGE
                        docker push $FRONTEND_IMAGE
                        """
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh """
                    kubectl set image deployment/backend backend=$BACKEND_IMAGE -n $K8S_NAMESPACE
                    kubectl set image deployment/frontend frontend=$FRONTEND_IMAGE -n $K8S_NAMESPACE
                    kubectl set image deployment/prometheus prometheus=$PROMETHEUS_IMAGE -n $K8S_NAMESPACE
                    kubectl set image deployment/grafana grafana=$GRAFANA_IMAGE -n $K8S_NAMESPACE
                    """
                }
            }
        }
        stage('Monitor and Validate') {
            steps {
                script {
                    sh "kubectl get pods -n $K8S_NAMESPACE"
                }
            }
        }
    }
    post {
        always {
            sh "docker logout"
        }
    }
}
