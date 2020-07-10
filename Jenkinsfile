pipeline {
    agent any
    stages {
        stage('Building') {
            steps {
            // One or more steps need to be included within the steps block.
            build job: 'TestP1',propagate:'false'
            build job: 'TestP2',propagate:'false'
            }
        }
    }
}
