
pipeline {
    agent {
        kubernetes {
            cloud 'minikube'
            yaml '''
apiVersion: v1
kind: Pod
spec:
  serviceAccountName: jenkins-agent
  containers:
    - name: python
      image: python:3.11-slim
      command:
        - sleep
      args:
        - 99d

    - name: kaniko
      image: gcr.io/kaniko-project/executor:v1.23.2-debug
      command:
        - /busybox/cat
      tty: true

    - name: kubectl
      image: alpine/k8s:1.34.1
      command:
        - /bin/sh
      args:
        - -c
        - sleep 99d
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

        stage('Build image') {
            steps {
                container('kaniko') {
                    withCredentials([
                        usernamePassword(
                            credentialsId: 'dockerhub-credentials',
                            usernameVariable: 'DOCKER_USER',
                            passwordVariable: 'DOCKER_TOKEN'
                        )
                    ]) {
                        sh '''
                            mkdir -p /kaniko/.docker

                            AUTH=$(printf '%s:%s' "$DOCKER_USER" "$DOCKER_TOKEN" | base64 | tr -d '\\n')

                            printf '{"auths":{"https://index.docker.io/v1/":{"auth":"%s"}}}' "$AUTH" > /kaniko/.docker/config.json

                            /kaniko/executor \
                              --context "$WORKSPACE" \
                              --dockerfile "$WORKSPACE/Dockerfile" \
                              --destination "moralis1995/ml-service:${BUILD_NUMBER}"
                        '''
                    }
                }
            }
        }

        stage('Check Kubernetes access') {
            steps {
                container('kubectl') {
                    sh '''
                        kubectl auth can-i patch deployments/ml-service
                        kubectl get deployment ml-service
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                container('kubectl') {
                    sh '''
                        kubectl set image deployment/ml-service \
                          ml-service=moralis1995/ml-service:${BUILD_NUMBER}

                        kubectl rollout status deployment/ml-service --timeout=180s
                    '''
                }
            }
        }

        stage('Smoke Test') {
            steps {
                container('python') {
                    sh '''
python - <<'PY'
import json
import urllib.request

url = "http://ml-service:5000/predict"

data = json.dumps({
    "age": 40,
    "purchase_amount": 300
}).encode()

request = urllib.request.Request(
    url,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(request, timeout=10) as response:
    assert response.status == 200
    result = json.load(response)

assert "probability" in result
assert isinstance(result["probability"], (int, float))
assert 0 <= result["probability"] <= 1

print("Smoke test PASSED:", result)
PY
'''
                }
            }
        }
    }
}
