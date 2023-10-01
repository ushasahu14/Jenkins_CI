pipeline {
    agent any
    parameters {
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
            }
        }
        stage("Test"){
           when {expression {params.ENVIRONMENT != "PRODUCTION"}}
           steps{
               echo "this is $params.ENVIRONMENT"
           }
        }
        stage("Deploy"){
           when{expression { params.ENVIRONMENT == "PRODUCTION"}}
           steps{
               
               echo "this is $params.ENVIRONMENT , $v1,$v2"
           }
        }

}
}