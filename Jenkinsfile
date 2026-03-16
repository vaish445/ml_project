pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Training Script') {
            steps {
                sh 'python3 src/model_training.py'
            }
        }

    }
}
