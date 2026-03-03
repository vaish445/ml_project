pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Training Script') {
            steps {
                sh 'python3 src/train.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: '**/*.pkl', fingerprint: true
            }
        }
    }
}
