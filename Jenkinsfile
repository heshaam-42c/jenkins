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
        //             args '-e SCAN_TOKEN=scan_cfc54641-c185-45ce-98a3-b3ac473f3fed -e PLATFORM_SERVICE=services.42crunch.com:8001'
        //         }
        //     }
        //     steps {

        //     }
        // }

        // docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:latest  --default-authentication-plugin=mysql_native_password
        stage("Conformance Scan") {
            steps {
                script {
                    docker.image('42crunch/scand-agent:latest').withRun('-e SCAN_TOKEN=scan_cfc54641-c185-45ce-98a3-b3ac473f3fed -e PLATFORM_SERVICE=services.42crunch.com:8001') {c ->
                        // Run command
                    }
                }
            }
        }
    }
}