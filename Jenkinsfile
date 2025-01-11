pipeline {
    agent any

    stages {
        stage('Verify Kubernetes Installation') {
            steps {
                script {
                    echo 'Checking kubectl installation...'
                    try {
                        sh 'kubectl version --client'
                    } catch (Exception e) {
                        error("Failed to verify kubectl installation. Ensure it is installed and accessible in the PATH.")
                    }
                }
            }
        }

        stage('Verify Docker') {
            steps {
                script {
                    echo 'Checking Docker installation...'
                    try {
                        sh 'docker --version'
                    } catch (Exception e) {
                        error("Failed to verify Docker installation. Ensure Docker is installed and accessible in the PATH.")
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            echo 'Pipeline failed. Please check the error logs above.'
        }
    }
}
