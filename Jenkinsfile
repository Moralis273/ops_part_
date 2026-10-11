
pipeline {
    agent {
        kubernetes {
            cloud 'minikube'
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: python
      image: python:3.11-slim
      command:
        - sleep
      args:
        - 99d
'''
            defaultContainer 'python'
        }
    }

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
                    python -m pip install -r requirements.txt pytest
                    python -m pytest -v
                '''
            }
        }
    }
}
