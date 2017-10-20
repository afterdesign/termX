pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
              def userInput = input(
                id: 'userInput',
                message: 'Let\'s promote?',
                parameters: [
                  [$class: 'StringParameterDefinition', description: 'Environment', name: 'env']
                ]
              )
              echo ("Env1: "+userInput['env'])
            }
        }
        stage('Print') {
          steps {
            echo ("Env2: "+userInput['env'])
          }
        }
    }
}
