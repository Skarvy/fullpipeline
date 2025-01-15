pipeline {
    agent any
    environment {
        K8S_NAMESPACE = 'mi-proyecto'
        DOCKER_USERNAME = 'skardevops'
        FRONTEND_IMAGE = "${DOCKER_USERNAME}/frontend:latest"
        BACKEND_IMAGE = "${DOCKER_USERNAME}/backend:latest"
        KIND_CLUSTER_NAME = 'mi-cluster'
        KUBECONFIG = '/var/jenkins_home/.kube/config'
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
        stage('Create Kind Cluster') {
    steps {
        script {
            sh """
            if ! kind get clusters | grep -q $KIND_CLUSTER_NAME; then
                kind create cluster --name $KIND_CLUSTER_NAME --config kind-cluster-config.yaml
            fi
            kind get kubeconfig --name $KIND_CLUSTER_NAME > /tmp/kind_kubeconfig
            export KUBECONFIG=/tmp/kind_kubeconfig
            """
        }
    }
}

stage('Deploy to Kubernetes') {
    steps {
        script {
            sh """
            export KUBECONFIG=/tmp/kind_kubeconfig
            kubectl create namespace $K8S_NAMESPACE || echo "Namespace $K8S_NAMESPACE already exists"
            kubectl apply -f ./k8s/ -n $K8S_NAMESPACE --validate=false
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
