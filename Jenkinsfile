pipeline {
	agent any

	environment{
		APPLI = "docksaficio/monapp"
	}

	parameters {
		string(
			name: 'VERSION',
			defaultValue: 'v0',
			description: 'Quelle version pousse-t-on ?'
		)

		booleanParam(
			name: 'Deploiement',
			defaultValue: false
		)
	}

	stages {
		stage("checkout") {
			steps {
				checkout scm
			}
		}
		
		
		stage("Test") {
			steps {
				sh 'python3 -m py_compile app.py'
			}
		}


		stage("Build") {
			steps {
				sh "docker build -t ${APPLI}:${params.VERSION} ."
			}
		}


		stage("Push AND Login") {
			steps {
                        	withCredentials([usernamePassword(
                                	credentialsId: 'MaCoToDocker',
                                	usernameVariable: 'DOCKER_USER',
                                	passwordVariable: 'DOCKER_PASS'
                        	)])
					
                        	{			
                                		retry(3){
                                        		timeout(time: 20, unit: 'SECONDS') {
                                                		sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                                        		}
                                		}
                                		retry(3){
                                        		timeout(time: 20, unit: 'SECONDS') {
                                                		sh "docker push ${APPLI}:${params.VERSION}"
                                        		}
                                		}
					
                        	}
			}
		}
			
		stage("Deploiement eventuel") {
        when {
                expression {
                        params.Deploiement
                }
        }

        steps{
                withCredentials(sshUserPrivateKey([
                        credentialsId: 'SSH',
                        userVariable: 'leuser',
                        keyFileVariable: 'SSKey'
                ]))

                        {
                                retry(3){
                                        timeout(time: 20, unit: 'SECONDS') {
                                                sh '''ssh -u '$leuser' -p '$SSKey' && cd fe && git pull && VERSION=5 docker compose up monapp>'''
                                        }
                                }
                        }
        }
	}
	}
}

