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
]) {
    sh '''
        echo "Webhook présent : ${DISCORD_WEBHOOK:+oui}"
        curl -I "$DISCORD_WEBHOOK"
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
