pipeline {
  agent any
  stages {
    stage('clone') {
      steps {
        input 'test'
        input(submitterParameter: 'branch', message: 'Select branch')
      }
    }
    stage('print message') {
      steps {
        echo '$test'
      }
    }
  }
}