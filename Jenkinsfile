pipeline {
    agent any


        stage('Verify Kubernetes Installation') {
            steps {
                script {
                    sh 'kubectl version --client'
                }
            }
        }

        stage('Verify Cluster Access') {
            steps {
                script {
                    sh 'kubectl cluster-info'
                }
            }
        }

        stage('List Pods') {
            steps {
                script {
                    sh 'kubectl get pods --all-namespaces'
                }
            }
        }
    }
}
