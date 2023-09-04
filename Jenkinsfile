pipeline {
    agent any

    environment {
        KEYS_PARAM = 'your_keys'
        VALUES_PARAM = 'your_values'
        NAME_PARAM = 'your_name'
        REPO_PARAM = 'your_repo'
        TAG_PARAM = 'your_tag'
        WORKSPACE = "${WORKSPACE}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout your code from the Git repository
                checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/Keerthiuvk/Reference_service.git']]])
            }
        }

        stage('Execute Python Script') {
            steps {
                script {
                    // Execute the Python script with environment variables
                    sh "python ${WORKSPACE}/replace.py"
                }
            }
        }
    }
}
