pipeline {
    agent any

    stages {
        stage('Verify Kubernetes Installation') {
            steps {
                // Verificar si kubectl está disponible
                script {
                    try {
                        sh 'kubectl version --client'
                    } catch (Exception e) {
                        error "kubectl no está instalado o no es accesible."
                    }
                }
            }
        }

        stage('Verify Cluster Access') {
            steps {
                // Verificar si se puede acceder al clúster de Kubernetes
                script {
                    try {
                        sh 'kubectl cluster-info'
                    } catch (Exception e) {
                        error "No se puede acceder al clúster de Kubernetes."
                    }
                }
            }
        }

        stage('List Pods') {
            steps {
                // Listar los pods en el clúster para verificar que el clúster es accesible
                script {
                    try {
                        sh 'kubectl get pods --all-namespaces'
                    } catch (Exception e) {
                        error "Error al listar los pods del clúster de Kubernetes."
                    }
                }
            }
        }
    }
}
