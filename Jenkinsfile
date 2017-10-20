pipeline {
  agent any
  stages {
    stage('Example') {
      steps {
        script {
            env.VERSION_TO_DEPLOY = input(
                message: 'Version to deploy',
                parameters: [
                    string(
                        name: 'Version to relink',
                        description: '',
                        defaultValue: 'latest'
                    )
                ]
            )
        }
        echo("${env.VERSION_TO_DEPLOY}")
      }
    }
  }
}
