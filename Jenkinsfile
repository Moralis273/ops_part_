pipeline {
    agent any

    stages {
        stage('Check files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt pytest
                    .venv/bin/python -m pytest -v
                '''
            }
        }
    }
}