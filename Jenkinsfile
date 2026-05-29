pipeline{
    agent any

    stages{
        stage('Install Dependency'){
            steps{
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests'){
            steps{
                sh 'pytest ./calci_test/test_app.py -v'
            }
        }
    }
    post{
        always{
                echo 'Pipeline Ran'
            
        }
        success{
            echo 'Pipeline Succeeded'
        }
        failure{
            echo 'Pipeline Failed'
        }
    }
}