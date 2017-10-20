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
            echo +test
            echo $test
            echo ${test}
          }
        }
        stage('Print') {
          steps {
            echo +test
            echo $test
            echo ${test}
          }
        }
    }
}
