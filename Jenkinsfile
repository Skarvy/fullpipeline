pipeline {
    agent any
    environment {
        // Define the namespace and app name
        K8S_NAMESPACE = 'mi-proyecto'
        FRONTEND_IMAGE = 'frontend:latest'
        BACKEND_IMAGE = 'backend:latest'
        GRAFANA_IMAGE = 'grafana/grafana:latest'
        PROMETHEUS_IMAGE = 'prom/prometheus:latest'
        KUBECTL_PATH = '/usr/local/bin/kubectl'  // Ruta donde se instalará kubectl
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from the repository
                git branch: 'main', url: 'https://github.com/Skarvy/fullpipeline.git'
            }
        }
        stage('Install kubectl') {
            steps {
                script {
                    sh '''
                        echo "Checking if kubectl exists..." 
                        if [ ! -f $KUBECTL_PATH ]; then
                            echo "Downloading kubectl..."
                            curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.31.0/bin/linux/amd64/kubectl
                            chmod +x kubectl
                            mv kubectl $KUBECTL_PATH
                        else
                            echo "kubectl already exists in $KUBECTL_PATH"
                        fi
                        echo "Adding kubectl to PATH..."
                        export PATH=$PATH:$KUBECTL_PATH
                        echo "kubectl is available at $KUBECTL_PATH"
                    '''
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    // Build backend Docker image
                    sh "docker build -t $BACKEND_IMAGE ./api"

                    // Build frontend Docker image
                    sh "docker build -t $FRONTEND_IMAGE ./web"
                }
            }
        }
        stage('Push Docker Images to Registry') {
            steps {
                script {
                    // Usar las credenciales almacenadas en Jenkins de manera segura
                    withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_TOKEN')]) {
                        sh """
                        echo $DOCKER_TOKEN | docker login -u skardevops --password-stdin
                        docker build -t skardevops/backend:latest ./api
                        docker build -t skardevops/frontend:latest ./web
                        docker push skardevops/backend:latest
                        docker push skardevops/frontend:latest
                        """
                    }
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
