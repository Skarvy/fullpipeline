pipeline {
    agent any

    environment {
        KUBECTL_VERSION = 'v1.26.0' // Define la versión de kubectl a usar
    }

    stages {
        stage('Install kubectl') {
            steps {
                script {
                    sh '''#!/bin/bash
                    curl -LO https://dl.k8s.io/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl
                    chmod +x ./kubectl
                    mv ./kubectl /usr/local/bin/kubectl
                    '''
                }
            }
        }

        stage('Verify Kubernetes Installation') {
            steps {
                script {
                    try {
                        sh 'kubectl version --client'
                    } catch (Exception e) {
                        error('kubectl is not installed correctly.')
                    }
                }
            }
        }

        stage('Verify Cluster Access') {
            steps {
                script {
                    try {
                        sh 'kubectl cluster-info'
                    } catch (Exception e) {
                        error('Unable to access Kubernetes cluster. Check your configuration.')
                    }
                }
            }
        }

        stage('List Pods') {
            steps {
                script {
                    try {
                        sh 'kubectl get pods --all-namespaces'
                    } catch (Exception e) {
                        error('Unable to list pods. Check cluster permissions.')
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
        failure {
            echo 'Pipeline failed. Check the logs for more details.'
        }
    }
}
