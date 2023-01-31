Setup instruction for using jenkins project 

pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/your_repo.git'
            }
        }
        
        stage('Build Application') {
            steps {
                sh 'python setup.py build'
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'master'
            }
            steps {
                sh './deploy.sh production'
            }
        }
    }
}
