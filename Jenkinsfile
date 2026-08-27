pipeline {
    agent any

    stages {

        stage('Normal Step') {
            steps {
		echo 'Étape normale'
            }
        }
    }



	post {

		failure {
		echo 'pipeline échoué'

			withCredentials([
    string(credentialsId: 'discord-webhook', variable: 'DISCORD_WEBHOOK')
]) {
    sh '''
        curl -X POST \
        -H 'Content-Type: application/json' \
        -d '{"content":"Job : '"$JOB_NAME"'\\nBuild : '"$BUILD_NUMBER"'\\nLien : '"$BUILD_URL"'"}' \
        "$DISCORD_WEBHOOK"
    '''
}

		}
		
		success {
			echo "le pipeline a reussi"

withCredentials([
    string(credentialsId: 'discord-webhook', variable: 'DISCORD_WEBHOOK')
]) {
    sh '''
        curl -X POST \
        -H 'Content-Type: application/json' \
        -d '{"content":"Job : '"$JOB_NAME"'\\nBuild : '"$BUILD_NUMBER"'\\nLien : '"$BUILD_URL"'"}' \
        "$DISCORD_WEBHOOK"
    '''
		}
		}
		always {
			echo "fin"
		}
		



	}
}
