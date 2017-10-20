pipeline {
  agent any
  stages {
    stage('clone') {
      steps {
        input(message: 'test', id: 'test', ok: 'test')
      }
    }
    stage('') {
      steps {
        echo '$test'
      }
    }
  }
}