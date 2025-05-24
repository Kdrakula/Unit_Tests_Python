pipeline {
    agent any

    environment {
        DEPLOY_TAG = "V1.0.${env.BUILD_NUMBER}"
        IMAGE_NAME = "kdrakula/unit-tests"
    }

    stages {
        stage("Build") {
            steps {
                echo "Build stage..."
                sh "docker build -t ${IMAGE_NAME}:${DEPLOY_TAG} -f build.Dockerfile ."
            }
        }

        stage("Test") {
            steps {
                echo "Test stage..."
                script {
                    sh "docker build -t ${IMAGE_NAME}:test -f test.Dockerfile ."
                    def testOutput = sh(script: "docker run --rm ${IMAGE_NAME}:test", returnStdout: true)
                    echo "Captured test output:\n${testOutput}"
                }
            }
        }
    }
}
