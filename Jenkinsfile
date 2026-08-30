pipeline {
    agent any

	parameters {
		choice(
			name: 'ENV',
			choices: ['dev', 'staging', 'prod']
		)

		booleanParam(
			name: 'PUSH_IMAGE',
			defaultValue: false
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
			echo 'le build est fait'
		}
	}

	stage("Push Image") {
		when {
			expression {
				params.PUSH_IMAGE
			}
		}
		steps {
			echo 'image est push'
		}
	}

	stage("Deploy") {
		when {
			expression {
				params.ENV == 'prod' && params.PUSH_IMAGE
			}
		}
		steps {
                        echo 'conteneur déployé'
                }
	}



     }


}
