pipeline {
    agent any
    stages {
        stage('Example') {
          steps {
            script {
              def env.VERSION_TO_DEPLOY = input message: 'Version to deploy',
              parameters: [
                string(
                  name: 'Branch to deploy',
                  description: 'What branch you wont deploy?',
                  defaultValue: 'latest'
                )
              ]
            }
            echo ${VERSION_TO_DEPLOY}
          }
        }
        stage('Print') {
          steps {
            echo $VERSION_TO_DEPLOY
          }
        }
    }
}
