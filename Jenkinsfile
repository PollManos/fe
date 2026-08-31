pipeline {
    agent any


	environment {
		MON_APPLI = 'docksaficio/monappamoi'
	}

	parameters {
		choice(
			name: 'ENV',
			choices: ['dev', 'staging', 'prod']
		)

		booleanParam(
			name: 'PUSH_IMAGE',
			defaultValue: false
		)

		string(
			name: 'version',
			defaultValue: 'v1',
			description: 'Quelle version pousse-t-on ?'
		)
		
	}


    stages {

        stage('Checkout') {
            steps {
		checkout scm	
	    }
	 }

	
	stage("Tests") {
		steps {
			sh "python3 app.py"		
		}
	}

	stage("Build image") {
		steps {
			sh "docker build -t ${MON_APPLI}:${params.version} ."	
		}
	}

	stage("Push DockerHub") {
		when {
			expression {
				params.PUSH_IMAGE && params.ENV == 'prod'
			}	
		}
		steps {
			withCredentials([
				usernamePassword(
					credentialsId: 'MaCoToDocker',
					usernameVariable: 'MonUser',
					passwordVariable: 'MonPass'
				)
			])
				{
				sh 'echo "$MonPass" | docker login -u "$MonUser" --password-stdin'
			retry(3) {
				timeout(time: 30, unit: 'SECONDS') {
					sh "docker push ${MON_APPLI}:${params.version}"
				}
			}		
		}
		}	
	}
   }
	
	post {
		success {
			withCredentials([
				string(
					credentialsId: 'discord-webhook',
					variable: 'discordw'
				)
			])
			{
				sh '''
					curl -X POST \
						-H 'Content-Type: application/json' \
						-d '{"content":"Pipeline réussi\\nJob: '"$JOB_NAME"'\\nBuild: '"$BUILD_NUMBER"'\\nLien: '"$BUILD_URL"'"}' \
						"$discordw"
				'''
			}
		}
		
		failure {
			withCredentials([
				string(
					credentialsId: 'discord-webhook',
					variable: 'discordw'
				)
			])
				{
				sh '''
					curl -X POST \
						-H "Content-Type: application/json" \
						-d '{"content":"Pipeline raté\\nJob: '"$JOB_NAME"'\\nBuild: '"$BUILD_NUMBER"'\\nLien: '"$BUILD_URL"'"}' \
						"$discordw"
				'''
				}
		}
	}
}
