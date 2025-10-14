pipeline {
  agent any

  environment {
    REGISTRY = 'docker.io'
    DOCKERHUB_CREDENTIALS = 'dockerhub-creds' 
    DOCKERHUB_NAMESPACE = 'iam-mahendravarma'

    FRONTEND_IMAGE = "${DOCKERHUB_NAMESPACE}/react-frontend"
    BACKEND_IMAGE  = "${DOCKERHUB_NAMESPACE}/python-backend"

    FRONTEND_CONTEXT = './frontend'
    BACKEND_CONTEXT  = './backend'

    IMAGE_TAG = "${env.BUILD_NUMBER}"
  }

  stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/iam-mahendravarma/DevOps-Project-03-Dockerized-Microservices.git
        }

    stage('Frontend Lint & Test') {
      steps {
        dir(env.FRONTEND_CONTEXT) {
          sh 'npm ci'
          sh 'npm run lint'
          sh 'npm run test:ci'
        }
      }
    }

    stage('Backend Lint & Test') {
      steps {
        dir(env.BACKEND_CONTEXT) {
          sh 'python -m venv .venv'
          sh '. .venv/bin/activate && pip install -U pip'
          sh '. .venv/bin/activate && pip install -r requirements.txt'
          sh '. .venv/bin/activate && pip install -U ruff black mypy pytest pytest-asyncio httpx'
          sh '. .venv/bin/activate && ruff check .'
          sh '. .venv/bin/activate && black --check .'
          sh '. .venv/bin/activate && pytest'
        }
      }
    }

    stage('Docker Build') {
      steps {
        dir(env.ROOT_CONTEXT) {
          sh 'docker build -t ${FRONTEND_IMAGE}:${IMAGE_TAG} -f frontend/Dockerfile frontend'
          sh 'docker build -t ${BACKEND_IMAGE}:${IMAGE_TAG} -f backend/Dockerfile backend'
        }
      }
    }

    stage('Docker Login & Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin ${REGISTRY}'
          sh 'docker push ${FRONTEND_IMAGE}:${IMAGE_TAG}'
          sh 'docker push ${BACKEND_IMAGE}:${IMAGE_TAG}'
        }
      }
    }

    stage('Deploy with Compose') {
      steps {
        dir(env.ROOT_CONTEXT) {
          sh 'docker compose pull || true'
          sh 'docker compose down'
          sh 'docker compose up -d --build'
        }
      }
    }
  }

  post {
    always {
      dir(env.BACKEND_CONTEXT) { sh 'rm -rf .venv || true' }
      sh 'docker logout ${REGISTRY} || true'
    }
  }
}


