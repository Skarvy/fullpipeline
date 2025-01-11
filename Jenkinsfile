pipeline {
    agent {
        docker {
            image 'jenkins-with-docker-and-kubectl:latest'
        }
    }

    stages {
        stage('Verify Kubernetes Installation') {
            steps {
                script {
                    sh 'kubectl version --client'
                }
            }
        }

        stage('Verify Docker') {
            steps {
                script {
                    sh 'docker --version'
                }
            }
        }
    }
}
