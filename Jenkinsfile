pipeline {
    agent any
    stage('Example') {
        steps {
            def userInput = input(id: 'userInput', message: 'Select the next stage:', parameters: [
                [$class: 'BooleanParameterDefinition', defaultValue: false, description: 'Run QA tests', name: 'QA'],
                [$class: 'BooleanParameterDefinition', defaultValue: false, description: 'Run performance tests', name: 'performance']
            ])
        }
    }
}
