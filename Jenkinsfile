pipeline {
    agent any

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
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Restart Application') {
            steps {
                sh '''
                [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
                pm2 restart flask-app || pm2 start "python3 app.py" --name flask-app
                '''
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python3 -m unittest discover'
                    } catch (Exception e) {
                        echo "⚠️ Tests failed: ${e}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
    }
}
