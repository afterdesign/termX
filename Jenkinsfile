pipeline {
    agent any
    stage('Example') {
        steps {
            script {
                env.VERSION_TO_DEPLOY = input message: 'Version to deploy',
                parameters: [
                    string(
                    name: 'Version to relink',
                    description: '',
                    defaultValue: 'latest'
                    )
                ]

                def test = "test"
            }
            echo("${env.VERSION_TO_DEPLOY}")
        }
    }
}
