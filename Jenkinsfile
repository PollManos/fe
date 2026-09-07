pipeline {
	agent any

	environment {
		APPLI = "docksaficio/monapp"
	}

	parameters {
		string(
			name: 'VERSION',
			defaultValue: 'v0',
			description: 'Quelle version pousser ?'
		)
	
		choice(
		name: 'ENV',
		choices ['dev', 'staging', 'prod']
		)
		
		boolean(
			name: 'PUSH_IMAGE',
			defaultValue: false
		)	
	}


	stages {

		stage("Tests") {
			steps {
				sh "python3 app.py" 
			}
		}

	
		stage("Build Image") {
			steps {
				sh "docker build -t ${APPLI}:${params.VERSION} ."
			}
		}


		stage("Push and Login") {
			when {
				expression {
					params.PUSH_IMAGE && params.ENV == "prod"
				}
			}
			steps {
				withCredentials([
					usernamePassword(
						credentialsId: "MaCoToDocker",
						usernameVariable: "MonUser",
						passwordVariable: "MonPass"
					)
				])
					{	retry(3) {
                                        		timeout(time: 30, unit: 'SECONDS') {
								sh 'echo $MonPass | docker login -u $MonUser --password-stdin'
							}
						}
						
						retry(3) {
							timeout(time: 40, unit: 'SECONDS') {
								sh "docker push ${APPLI}:${params.VERSION}" 
							}
						}
					}
			}
		}
	}		

		post {

						// Message envoyé à Discord en cas de succès				
			success {
				withCredentials([
					string(
						credentialsId: "discord-webhook",
						variable: "discordW"
					)
				])

					{
						sh '''
							curl -X POST \
								-H "Content-Type: application/json" \
								-d '{"content":"Pipeline réussi:\\nJob: '"$JOB_NAME"'\\nBuild: '"$BUILD_NUMBER"'\\nLien: '"$BUILD_URL"'"}' \
								$discordW		
						'''
					}
			}


						//Message envoyé à Discord en cas d'échec
			failure {
				withCredentials([
                                        string(
                                                credentialsId: "discord-webhook",
                                                variable: "discordW"
                                        )
                                ])
				
					{
						sh '''
                                                        curl -X POST \
                                                                -H "Content-Type: application/json" \
                                                                -d '{"content":"Pipeline raté:\\nJob: '"$JOB_NAME"'\\nBuild: '"$BUILD_NUMBER"'\\nLien: '"$BUILD_URL"'"}' \
                                                                $discordW
                                                '''
					}
			}
		}
}
