pipeline {
    agent any

    stages {
        stage('Update YAML Files') {
            steps {
                script {
                    // Clone your repository or set up your workspace here
                    
                    // Define environment variables
                    env.KEYS_PARAM = "env,iam_config,dbsecret,replicaCount,probePath,labels"
                    env.VALUES_PARAM = "value1,value2,value3,value4,value5"
                    env.NAME_PARAM = "new_name"
                    env.REPO_PARAM = "new_repository"
                    env.TAG_PARAM = "new_tag"
                    
                    // Run the Python script
                    checkout scm
                    sh 'python3 replace.py'
                }
            }
        }
    }
}
