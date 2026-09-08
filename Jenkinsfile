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
                                	usernameVariable: "User",
                                	passwordVariable: "Pass"
                        	)])
					
				
                        	{
					sh '''
    if [ -n "$User" ]; then
        echo "User présent"
    else
        echo "User VIDE"
    fi
'''
                                	retry(3){
                                        	timeout(time: 20, unit: 'SECONDS') {
                                                	sh 'echo "$Pass" | docker login -u "$User" --password-stdin'
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
			steps {
				sh "VERSION=${params.VERSION} docker compose up -d"
			}
		}
	}
}
