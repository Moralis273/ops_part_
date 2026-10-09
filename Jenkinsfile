pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Moralis273/ops_part_.git'
            }
        }

        stage('Check files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }
    }
}