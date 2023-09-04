pipeline {
    agent any

    environment {
        REFERENCE_REPO = 'https://github.com/Keerthiuvk/Reference_service.git'
        REFERENCE_BRANCH = 'main'
        NEW_NAME = 'new-service-name'
        NEW_TAG = 'v2.0'
        NEW_IMAGE = 'your-registry/your-image:v2.0'
        WORKSPACE_DIR = "${WORKSPACE}/temp"
    }
    
    stages {
        stage('Clone Reference Repository') {
            steps {
                dir(WORKSPACE_DIR) {
                    git branch: REFERENCE_BRANCH, credentialsId: 'keerthi-git', url: REFERENCE_REPO
                }
            }
        }

        stage('Modify YAML Files') {
            steps {
                script {
                    // Navigate to the directory with YAML files
                    dir(WORKSPACE_DIR) {
                        // Loop through YAML files and modify them
                        sh """
                            find . -name '*.yaml' -print0 | xargs -0 sed -i 's/old-service-name/${NEW_NAME}/g'
                            find . -name '*.yaml' -print0 | xargs -0 sed -i 's/old-tag/${NEW_TAG}/g'
                            find . -name '*.yaml' -print0 | xargs -0 sed -i 's#old-image#${NEW_IMAGE}#g'
                        """
                    }
                }
            }
        }

        stage('Commit and Push Changes') {
            steps {
                dir(WORKSPACE_DIR) {
                    sh '''
                        git config user.email "keerthi25u@gmail.com"
                        git config user.name "Keerthi"
                        git add .
                        git commit -m "Update YAML files"
                        git push -u origin main
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                sh "rm -rf ${WORKSPACE_DIR}"
            }
        }
    }
}
