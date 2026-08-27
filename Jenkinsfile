pipeline {
    agent any

    stages {

        stage('Normal Step') {
            steps {
		echo 'Étape normale'
            }
        }

        stage('Hard Failure') {
            steps {
                sh 'exit 1'
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
					-d "{\"content\": \"Job : $JOB_NAME\"}" \
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
}
