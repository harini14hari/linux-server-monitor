pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Environment Check') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
            }
        }

        stage('Python Validation') {
            steps {
                sh 'python3 -m py_compile python/*.py'
            }
        }

        stage('Project Review') {
            steps {
                sh 'ls -la'
                sh 'ls -la python/'
            }
        }

        stage('Completed') {
            steps {
                echo 'Linux Monitoring CI Pipeline Completed!'
            }
        }
    }
}
