pipeline {
    agent any
    environment {
        K8S_NAMESPACE = 'mi-proyecto'
        DOCKER_USERNAME = 'skardevops'
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
        stage('Update Manifests') {
            steps {
                script {
                    sh """
                    sed -i 's|image: .*backend:.*|image: $BACKEND_IMAGE|' ./k8s/backend-deployment.yaml
                    sed -i 's|image: .*frontend:.*|image: $FRONTEND_IMAGE|' ./k8s/frontend-deployment.yaml
                    """
                }
            }
        }
        stage('Apply Kubernetes Manifests') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'kubeconfig-file', variable: 'KUBECONFIG')]) {
                        sh """
                        export KUBECONFIG=${KUBECONFIG}
                        kubectl apply -f ./k8s/ -n $K8S_NAMESPACE
                        """
                    }
                }
            }
        }
        stage('Monitor and Validate') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'kubeconfig-file', variable: 'KUBECONFIG')]) {
                        sh """
                        export KUBECONFIG=${KUBECONFIG}
                        kubectl get pods -n $K8S_NAMESPACE
                        """
                    }
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
