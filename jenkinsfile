pipeline {
    agent any
    environment {
        // Define the namespace and app name
        K8S_NAMESPACE = 'mi-proyecto'
        FRONTEND_IMAGE = 'frontend:latest'
        BACKEND_IMAGE = 'backend:latest'
        GRAFANA_IMAGE = 'grafana/grafana:latest'
        PROMETHEUS_IMAGE = 'prom/prometheus:latest'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from the repository
                git branch: 'main', url: 'https://github.com/Skarvy/fullpipeline.git'
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    // Build backend Docker image
                    sh "docker build -t $BACKEND_IMAGE ./backend"

                    // Build frontend Docker image
                    sh "docker build -t $FRONTEND_IMAGE ./frontend"
                }
            }
        }
        stage('Push Docker Images to Registry') {
            steps {
                script {
                    // Log in to DockerHub or any container registry you are using
                    sh "docker login -u \$DOCKER_USERNAME -p \$DOCKER_PASSWORD"

                    // Push backend Docker image to DockerHub or any registry
                    sh "docker push $BACKEND_IMAGE"

                    // Push frontend Docker image to DockerHub or any registry
                    sh "docker push $FRONTEND_IMAGE"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Deploy the backend app in Kubernetes
                    sh """
                    kubectl set image deployment/backend backend=$BACKEND_IMAGE -n $K8S_NAMESPACE
                    """

                    // Deploy the frontend app in Kubernetes
                    sh """
                    kubectl set image deployment/frontend frontend=$FRONTEND_IMAGE -n $K8S_NAMESPACE
                    """

                    // Deploy Prometheus
                    sh """
                    kubectl set image deployment/prometheus prometheus=$PROMETHEUS_IMAGE -n $K8S_NAMESPACE
                    """

                    // Deploy Grafana
                    sh """
                    kubectl set image deployment/grafana grafana=$GRAFANA_IMAGE -n $K8S_NAMESPACE
                    """
                }
            }
        }
        stage('Monitor and Validate') {
            steps {
                script {
                    // Here you can add steps to monitor the pods, check logs, or validate the deployments
                    sh "kubectl get pods -n $K8S_NAMESPACE"
                }
            }
        }
    }
    post {
        always {
            // Cleanup steps, like logging out from the Docker registry
            sh "docker logout"
        }
    }
}
