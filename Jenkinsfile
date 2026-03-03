pipeline {
    agent any

    stages {

        stage('Install Python & Dependencies') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                pip3 install -r requirements.txt
                '''
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
