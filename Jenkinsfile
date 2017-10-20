pipeline {
  agent any
  stages {
    stage('clone') {
      steps {
        input(
          id: 'Proceed1',
          message: 'Was this successful?',
          parameters: [
            [
              $class: 'StringParameterDefinition',
              description: '',
              name: 'Please confirm you agree with this'
            ]
        ])
      }
    }
    stage('print message') {
      steps {
        echo '$test'
      }
    }
  }
}
