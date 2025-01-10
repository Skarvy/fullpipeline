pipeline {
    agent any

    stage('Install kubectl') {
        steps {
            script {
                sh '''#!/bin/bash
                curl -LO https://dl.k8s.io/release/v1.26.0/bin/linux/amd64/kubectl
                chmod +x ./kubectl
                mv ./kubectl /usr/local/bin/kubectl
                '''
            }
        }
    }

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
