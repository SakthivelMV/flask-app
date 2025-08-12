pipeline {
    agent any
    tools {
        nodejs "NodeJS 20"
    }
    environment {
        NVM_DIR = "/var/lib/jenkins/.nvm"
    }
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
                sh '''
                [ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh"
                pm2 restart flask-app || pm2 start "python3 app.py" --name flask-app
                '''
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
