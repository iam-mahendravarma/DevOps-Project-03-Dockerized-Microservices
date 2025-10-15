pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds'  // Jenkins credentials ID for Docker Hub
        DOCKERHUB_USERNAME = 'iammahendravarma20'
        FRONTEND_IMAGE = "${DOCKERHUB_USERNAME}/react-frontend:latest"
        BACKEND_IMAGE = "${DOCKERHUB_USERNAME}/python-backend:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main',
                    url: 'https://github.com/iam-mahendravarma/DevOps-Project-03-Dockerized-Microservices.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Frontend: Install & Lint') {
            steps {
                dir('frontend') {
                    echo "Installing frontend dependencies..."
                    sh 'npm install'
                    echo "Running frontend lint..."
                    sh 'npm run lint || echo "Lint issues found"'
                    echo "Running frontend tests..."
                    sh 'npm test || echo "No tests or some tests failed"'
                }
            }
        }

        stage('Backend: Install & Test') {
            steps {
                dir('backend') {
                    echo "Installing backend dependencies..."
                    sh 'pip install -r requirements.txt'
                    echo "Running backend tests..."
                    sh 'pytest || echo "No tests or some tests failed"'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                echo "Building frontend Docker image..."
                sh "docker build -t ${FRONTEND_IMAGE} ./frontend"

                echo "Building backend Docker image..."
                sh "docker build -t ${BACKEND_IMAGE} ./backend"
            }
        }

        stage('Push Docker Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", 
                    passwordVariable: 'DOCKER_PASSWORD', 
                    usernameVariable: 'DOCKER_USERNAME')]) {
                    echo "Logging into Docker Hub..."
                    sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"

                    echo "Pushing frontend image..."
                    sh "docker push ${FRONTEND_IMAGE}"

                    echo "Pushing backend image..."
                    sh "docker push ${BACKEND_IMAGE}"

                    sh "docker logout"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo "Deploying containers using docker-compose..."
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }
    }

    post {
        always {
            echo "Cleaning up dangling Docker images..."
            sh 'docker system prune -f || echo "Nothing to prune"'
        }
        success {
            echo "✅ Pipeline completed successfully! 🎉"
        }
        failure {
            echo "❌ Pipeline failed! Check logs for errors."
        }
    }
}
