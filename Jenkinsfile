pipeline {
    agent any

    environment {
        K8S_NAMESPACE = 'default'
        KUBECONFIG_CONTENT = '''apiVersion: v1
        clusters:
        - cluster:
            server: https://<API_SERVER_URL>
            certificate-authority-data: <CERTIFICATE_AUTHORITY_DATA>
        contexts:
        - context:
            cluster: <CLUSTER_NAME>
            user: <USER_NAME>
        current-context: <CLUSTER_NAME>
        kind: Config
        preferences: {}
        users:
        - name: <USER_NAME>
          user:
            client-certificate-data: <CLIENT_CERTIFICATE_DATA>
            client-key-data: <CLIENT_KEY_DATA>
        '''
        KUBECONFIG = '/var/jenkins_home/.kube/config'
    }

    stages {
        stage('Generar kubeconfig') {
            steps {
                script {
                    // Escribir el archivo kubeconfig en el directorio adecuado
                    writeFile file: KUBECONFIG, text: KUBECONFIG_CONTENT
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
