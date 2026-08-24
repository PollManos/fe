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
		timeout(time: 30, unit: 'SECONDS') {
                	sh 'sleep 20'
		}
            }
        }

        stage('Flaky Operation') {
            steps {
		retry(3) {
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
        }


	stage('Notification') {
	    steps {
        	sh 'exit 1'
    		}
	}

        stage('Hard Failure') {
            steps {
                sh 'exit 1'
            }
        }
    }
}
