pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
              input(
                id: 'userInput',
                message: 'Let\'s promote?',
                parameters: [
                  [$class: 'StringParameterDefinition', description: 'Environment', name: 'env']
                ]
              )
              echo "Hello"
            }
        }
    }
}
