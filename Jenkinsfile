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
        	catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
		sh 'exit 1'
		}		
    		}
	}

        stage('Hard Failure') {
            steps {
                sh 'exit 1'
            }
        }
    }
}



	post {

		failure {
			withCredentials([
				string(credentialsId: 'discord-webhook', variable: 'DISCORD_WEBHOOK')
			])

			{
			 	sh '''
					curl -X POST \
					-H 'Content-type: application/json' \
					-d '{"content": "le pipeline a échoué"}' \
					"$DISCORD_WEBHOOK"
				'''

			}

		}
		
		success {
			echo "le pipeline a reussi"
		}

		always {
			echo "fin"
		}
		



	}
