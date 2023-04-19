pipeline {
    agent any 
    
    environment {
        GIT_URL = 'https://github.com/heshaam-42c/jenkins'
        GIT_BRANCH = 'main'
    }

    stages {
        stage('Audit OpenAPI files') {
            steps {
                audit repositoryName: "${GIT_URL}", branchName: "${GIT_BRANCH}", credentialsId: '42ctoken', minScore: 75, platformUrl: 'https://platform.42crunch.com', logLevel: 'DEBUG'
            }
        }
    }
}