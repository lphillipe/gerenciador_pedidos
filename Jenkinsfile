pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lphillipe/gerenciador_pedidos.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}