pipeline { 
agent any
    stages {
        stage('Cloning the Repository') {
            steps {
                git 'https://github.com/shivgarg05/jenkins-demo-1.git'
            }
        }
        stage('Executing Main') {
            steps {
		sh "chmod u+x main.py"
                sh "python3 main.py"
            }
        }
     stage('Run and Check Tests') {
            steps {
		sh "chmod u+x test.py"
                sh "python3 test.py"
            }
        }
    } 
}
