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
  post {  
      always {  
          echo 'This will always run'  
      }  
      success {  
          mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "SUCCESS CI: Project name -> ${env.JOB_NAME}", to: "ghazishazanahmad@gmail.com";  
      }  
      failure {  
          mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "ghazishazanahmad@gmail.com";  
      }  
      unstable {  
          echo 'This will run only if the run was marked as unstable'  
      }  
      changed {  
          echo 'This will run only if the state of the Pipeline has changed'  
          echo 'For example, if the Pipeline was previously failing but is now successful'  
            }  
     }
}
