pipeline {
    agent any 
    
    environment {
        GIT_URL = 'https://github.com/heshaam-42c/jenkins'
        GIT_BRANCH = 'main'
    }

    stages {
        stage('Run Python script') {
            steps {
                // Execute the Python script and capture the output
                script {
                    def scriptOutput = sh(script: 'python3 fetchOAS.py', returnStdout: true).trim()
                    // Set the environment variable with the script output
                    withEnv(["SCRIPT_OUTPUT=${scriptOutput}"]) {
                        echo "Script output: ${scriptOutput}"
                    }
                }
            }
        }

        stage('Audit OpenAPI files') {
            steps {
                audit repositoryName: "${env.GIT_URL}", branchName: "${env.GIT_BRANCH}", credentialsId: '42ctoken', minScore: 75, platformUrl: 'https://platform.42crunch.com', logLevel: 'DEBUG'
            }
        }
    }
}