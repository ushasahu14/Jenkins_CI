
pipeline {
    agent any
    options {timeout(time:1,unit:"HOURS")}
    parameters {
        string(name:"newname",defaultValue="x")
        choice( name:"ENVIRONMENT",
                choices:["DEVELOPMENT" ,"STAGING" ,"PRODUCTION"],
                description:"these are the choices")
        
        password(name:"APIKEY",
                defaultValue:"myname",
                description:"This is password")
        text(name:"Changelog",
            defaultValue:"this is log",
            description:"this is text")

   
          }

    stages {
        stage ("Git Checkout"){
            steps{
                git branch: 'main', credentialsId: 'gitlogin', poll: false, url: 'https://github.com/ushasahu14/Jenkins_CI.git'
            }
        }
        
               
        stage('Build') {
            steps {
                echo 'Hello World'
                sh "python3 helloworld.py"
                script{
                var1 =  sh (returnStdout:true, script:"echo 1").trim()
                }
            }
        }
        stage("Test"){
           when {expression {params.ENVIRONMENT != "PRODUCTION"}}
           steps{
               echo "this is $params.ENVIRONMENT"
               echo "${var1}"
           }
        }
        stage("Deploy"){
           when{expression { params.ENVIRONMENT == "PRODUCTION"}}
           steps{
               
               echo "this is $params.ENVIRONMENT , $var1"
           }
        }

}
}