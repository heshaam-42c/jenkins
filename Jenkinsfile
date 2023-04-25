pipeline {
    agent any {
      docker {
        image 'python:3'
        label 'my-build-agent'
      }
    }

    stages {
        stage('Run Python script') {
            steps {
                // Execute the Python script and capture the output
                script {
                    def scriptOutput = sh(script: 'python fetchOAS.py', returnStdout: true).trim()
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