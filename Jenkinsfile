pipeline {
    agent any
    stages {
        stage('Pull Code') {
            steps {
                git url: 'https://github.com/SakthivelMV/flask-app.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Restart Application') {
            steps {
                sh 'pm2 restart flask-backend || pm2 start "python3 app.py" --name flask-backend'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover || true'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed'
        }
    }
}
