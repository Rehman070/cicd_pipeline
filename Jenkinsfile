pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Build steps - Add your build commands here
                script {
                    echo 'Building the application...'
                    // Example build command: 'npm install' for Node.js projects
                }
            }
        }

        stage('Test') {
            steps {
                // Test steps - Add your test commands here
                script {
                    echo 'Running tests...'
                    // Example test command: 'npm test' for Node.js projects
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deployment steps - Add your deployment commands here
                script {
                    echo 'Deploying the application...'
                    // Example deployment command: 'docker-compose up -d' for Docker-based projects
                }
            }
        }
    }

    post {
        failure {
            // Rollback logic - Add your rollback commands here
            script {
                echo 'Rolling back the deployment...'
                // Example rollback command: 'docker-compose down' for Docker-based projects
            }
        }
    }
}
