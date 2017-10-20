pipeline {
    agent any
    stages {
        stage('Example') {
          steps {
            userInput = input(
              id: 'userInput',
              message: 'Let\'s promote?',
              parameters: [
                [$class: 'StringParameterDefinition', description: 'Environment', name: 'test']
              ]
            )
            echo (userInput['test'])
          }
        }
        stage('Print') {
          steps {
            echo (userInput['test'])
          }
        }
    }
}
