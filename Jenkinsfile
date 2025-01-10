pipeline {
    agent any
    stages {
        stage('Verify Docker') {
            steps {
                script {
                    echo "Checking Docker installation and version..."
                }
                sh '''
                # Check if Docker CLI is available
                docker --version

                # Run a simple Docker command to verify connectivity to the Docker daemon
                docker run hello-world
                '''
            }
        }
    }
}
