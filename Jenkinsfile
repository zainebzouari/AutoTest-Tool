pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/zainebzouari/AutoTest-Tool.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                bat 'echo Build step'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest --junitxml=results.xml --html=Report.html --alluredir=allure-results'
            }
        }

        stage('Save Results') {
            steps {
                junit 'results.xml'
                archiveArtifacts artifacts: 'Report.html', allowEmptyArchive: true
            }
        }
    }
}
