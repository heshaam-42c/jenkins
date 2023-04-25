pipeline {
    agent any
    
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

        // stage('Audit OpenAPI files') {
        //     steps {
        //         audit repositoryName: "${env.GIT_URL}", branchName: "${env.GIT_BRANCH}", credentialsId: '42ctoken', minScore: 75, platformUrl: 'https://platform.42crunch.com', logLevel: 'DEBUG'
        //     }
        // }

        // stage('Build') {
        //     agent {
        //         docker {
        //             image '42crunch/scand-agent:latest'
        //             args '-e SCAN_TOKEN=scan_20ff1cf0-1cc1-4b1f-8dde-2354e6a8a18f -e PLATFORM_SERVICE=services.42crunch.com:8001'
        //         }
        //     }
        //     steps {
        //         ls -la
        //     }
        // }

        // docker run --network="host" -e SCAN_TOKEN=scan_20ff1cf0-1cc1-4b1f-8dde-2354e6a8a18f -e PLATFORM_SERVICE=services.42crunch.com:8001 42crunch/scand-agent:latest
        stage("Conformance Scan") {
            steps {
                script {
                    docker.image('42crunch/scand-agent:latest').withRun('-e SCAN_TOKEN=scan_20ff1cf0-1cc1-4b1f-8dde-2354e6a8a18f -e PLATFORM_SERVICE=services.42crunch.com:8001', '--network="host"') {c ->
                        // Run command
                    }
                }
            }
        }
    }
}