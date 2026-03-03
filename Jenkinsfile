pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Training Script') {
            steps {
                sh 'python src/train.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: '**/*.pkl', fingerprint: true
            }
        }
    }
}
