pipeline {
    agent any

    stages {

        stage('Normal Step') {
            steps {
		echo 'Étape normale'
            }
        }

        stage('Slow Operation') {
            steps {
		timeout(time: 5, unit: 'SECONDS') {
                	sh 'sleep 20'
		}
            }
        }

        stage('Flaky Operation') {
            steps {
                sh '''
                    if [ ! -f /tmp/retry-demo ]; then
                        touch /tmp/retry-demo
                        echo "Temporary failure"
                        exit 1
                    fi

                    echo "Operation succeeded"
                '''
            }
        }

        stage('Hard Failure') {
            steps {
                sh 'exit 1'
            }
        }
    }
}
