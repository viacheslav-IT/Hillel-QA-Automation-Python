pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest lesson_31/ --junitxml=result.xml || true
                '''
            }
        }
    }

    post {
        always {
            junit 'result.xml'

            emailext to: 'dykyi.viacheslav@gmail.com',
                     subject: "Build Status: ${currentBuild.currentResult} - Job '${env.JOB_NAME}' [Build #${env.BUILD_NUMBER}]",
                     body: """
                         Pipeline completed with status: ${currentBuild.currentResult}
                         Project: ${env.JOB_NAME}
                         Build number: ${env.BUILD_NUMBER}
                         Results URL: ${env.BUILD_URL}
                     """
        }
    }
}