pipeline {
    agent any
    environment {
        K8S_NAMESPACE = 'mi-proyecto'
        DOCKER_USERNAME = 'skardevops' // Tu usuario en Docker Hub
        FRONTEND_IMAGE = "${DOCKER_USERNAME}/frontend:latest"
        BACKEND_IMAGE = "${DOCKER_USERNAME}/backend:latest"
        GRAFANA_IMAGE = 'grafana/grafana:latest'
        PROMETHEUS_IMAGE = 'prom/prometheus:latest'
        KUBECONFIG_PATH = "/var/jenkins_home/kubeconfig" // Ruta donde guardaremos el kubeconfig
    }
    stages {
        stage('Setup Control Plane') {
            steps {
                script {
                    sh """
                    # Instalar dependencias para Kubernetes
                    sudo apt-get update && sudo apt-get install -y kubeadm kubectl kubelet

                    # Inicializar el Control Plane si no está configurado
                    if ! sudo kubeadm config view &>/dev/null; then
                        sudo kubeadm init --pod-network-cidr=192.168.0.0/16

                        # Configurar acceso local para kubectl
                        mkdir -p $HOME/.kube
                        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
                        sudo chown $(id -u):$(id -g) $HOME/.kube/config

                        # Guardar kubeconfig para Jenkins
                        cp $HOME/.kube/config ${KUBECONFIG_PATH}
                    fi

                    # Instalar plugin de red (Calico)
                    kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml --kubeconfig=${KUBECONFIG_PATH}
                    """
                }
            }
        }
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
                    withCredentials([file(credentialsId: 'kubeconfig-file', variable: 'KUBECONFIG')]) {
                        sh """
                        kubectl set image deployment/backend backend=$BACKEND_IMAGE -n $K8S_NAMESPACE --kubeconfig=${KUBECONFIG}
                        kubectl set image deployment/frontend frontend=$FRONTEND_IMAGE -n $K8S_NAMESPACE --kubeconfig=${KUBECONFIG}
                        kubectl set image deployment/prometheus prometheus=$PROMETHEUS_IMAGE -n $K8S_NAMESPACE --kubeconfig=${KUBECONFIG}
                        kubectl set image deployment/grafana grafana=$GRAFANA_IMAGE -n $K8S_NAMESPACE --kubeconfig=${KUBECONFIG}
                        """
                    }
                }
            }
        }
        stage('Monitor and Validate') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'kubeconfig-file', variable: 'KUBECONFIG')]) {
                        sh "kubectl get pods -n $K8S_NAMESPACE --kubeconfig=${KUBECONFIG}"
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
