pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Verifica se está utilizando a branch correta
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t gerenciador_pedidos .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}