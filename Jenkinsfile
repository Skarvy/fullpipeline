pipeline {
    agent any

    environment {
        K8S_NAMESPACE = 'default'  // Puedes cambiar esto a tu namespace si es necesario
    }

    stages {
        stage('Verificar conexión con Kubernetes') {
            steps {
                script {
                    // Verificar que Jenkins pueda ejecutar kubectl
                    sh 'kubectl version --client'
                }
            }
        }

        stage('Listar Pods en Kubernetes') {
            steps {
                script {
                    // Listar los pods en el namespace por defecto
                    sh 'kubectl get pods -n $K8S_NAMESPACE'
                }
            }
        }

        stage('Verificar Estado de Nodes') {
            steps {
                script {
                    // Verificar el estado de los nodos en el clúster
                    sh 'kubectl get nodes'
                }
            }
        }
    }
}
