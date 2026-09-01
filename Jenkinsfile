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
                    python3 -m venv venv || python -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        ./venv/bin/pip install -r requirements.txt
                    else
                        ./venv/bin/pip install pytest
                    fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest lesson_31/ --junitxml=result.xml'
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