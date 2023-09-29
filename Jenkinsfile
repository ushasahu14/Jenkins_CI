pipeline {
    agent none
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
        input {message:"enter your input", 
               ok "go ahead"
               string(name:"INPUT",defaultValue:"Usha")
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