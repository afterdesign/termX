pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
              input(
                id: 'userInput',
                message: 'Let\'s promote?',
                parameters: [
                  [$class: 'StringParameterDefinition', description: 'Environment', name: 'test']
                ]
              )
              echo "Hello ${params.test}"
            }
        }
        stage('Print') {
          steps {
            echo "Hello ${params.test}"
          }
        }
    }
}
