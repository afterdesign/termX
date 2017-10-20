pipeline {
  agent any
  stages {
    stage('clone') {
      steps {
        input 'test'
      }
    }
    stage('print message') {
      steps {
        echo '$test'
      }
    }
  }
}