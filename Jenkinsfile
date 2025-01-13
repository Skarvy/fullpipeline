pipeline {
    agent any

    parameters {
        string(name: 'API_SERVER_URL', defaultValue: '', description: 'URL del servidor API de Kubernetes')
        string(name: 'CERTIFICATE_AUTHORITY_DATA', defaultValue: '', description: 'Datos de la autoridad certificadora')
        string(name: 'CLUSTER_NAME', defaultValue: '', description: 'Nombre del clúster de Kubernetes')
        string(name: 'USER_NAME', defaultValue: '', description: 'Nombre del usuario')
        string(name: 'CLIENT_CERTIFICATE_DATA', defaultValue: '', description: 'Certificado del cliente')
        string(name: 'CLIENT_KEY_DATA', defaultValue: '', description: 'Clave del cliente')
        string(name: 'DOCKER_USERNAME', defaultValue: 'skardevops', description: 'Tu usuario en Docker Hub')
        string(name: 'FRONTEND_IMAGE', defaultValue: 'skardevops/frontend:latest', description: 'Imagen del Frontend')
        string(name: 'BACKEND_IMAGE', defaultValue: 'skardevops/backend:latest', description: 'Imagen del Backend')
        string(name: 'GRAFANA_IMAGE', defaultValue: 'grafana/grafana:latest', description: 'Imagen de Grafana')
        string(name: 'PROMETHEUS_IMAGE', defaultValue: 'prom/prometheus:latest', description: 'Imagen de Prometheus')
        string(name: 'K8S_NAMESPACE', defaultValue: 'mi-proyecto', description: 'Nombre del namespace en Kubernetes')
    }

    environment {
        // Variables para el kubeconfig
        KUBECONFIG_API_SERVER = "${params.API_SERVER_URL}"
        KUBECONFIG_CA_DATA = "${params.CERTIFICATE_AUTHORITY_DATA}"
        KUBECONFIG_CLUSTER_NAME = "${params.CLUSTER_NAME}"
        KUBECONFIG_USER_NAME = "${params.USER_NAME}"
        KUBECONFIG_CLIENT_CERT_DATA = "${params.CLIENT_CERTIFICATE_DATA}"
        KUBECONFIG_CLIENT_KEY_DATA = "${params.CLIENT_KEY_DATA}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Skarvy/fullpipeline.git'
            }
        }

        stage('Generar kubeconfig') {
            steps {
                script {
                    // Crear el contenido del kubeconfig con los parámetros
                    def kubeconfigContent = """
                    apiVersion: v1
                    clusters:
                    - cluster:
                        server: ${env.KUBECONFIG_API_SERVER}
                        certificate-authority-data: ${env.KUBECONFIG_CA_DATA}
                    contexts:
                    - context:
                        cluster: ${env.KUBECONFIG_CLUSTER_NAME}
                        user: ${env.KUBECONFIG_USER_NAME}
                    current-context: ${env.KUBECONFIG_CLUSTER_NAME}
                    kind: Config
                    preferences: {}
                    users:
                    - name: ${env.KUBECONFIG_USER_NAME}
                      user:
                        client-certificate-data: ${env.KUBECONFIG_CLIENT_CERT_DATA}
                        client-key-data: ${env.KUBECONFIG_CLIENT_KEY_DATA}
                    """

                    // Escribir el archivo kubeconfig
                    writeFile file: '/tmp/.kube/config', text: kubeconfigContent


                    // Verificar que kubectl funcione con el kubeconfig
                    sh 'kubectl get nodes'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    sh "docker build -t ${params.BACKEND_IMAGE} ./api"
                    sh "docker build -t ${params.FRONTEND_IMAGE} ./web"
                }
            }
        }

        stage('Push Docker Images to Registry') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin"
                        sh "docker push ${params.BACKEND_IMAGE}"
                        sh "docker push ${params.FRONTEND_IMAGE}"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh """
                    kubectl set image deployment/backend backend=${params.BACKEND_IMAGE} -n ${params.K8S_NAMESPACE}
                    kubectl set image deployment/frontend frontend=${params.FRONTEND_IMAGE} -n ${params.K8S_NAMESPACE}
                    kubectl set image deployment/prometheus prometheus=${params.PROMETHEUS_IMAGE} -n ${params.K8S_NAMESPACE}
                    kubectl set image deployment/grafana grafana=${params.GRAFANA_IMAGE} -n ${params.K8S_NAMESPACE}
                    """
                }
            }
        }

        stage('Monitor and Validate') {
            steps {
                script {
                    sh "kubectl get pods -n ${params.K8S_NAMESPACE}"
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
