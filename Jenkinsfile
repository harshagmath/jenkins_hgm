pipeline{
    agent any

    triggers{
        pollSCM('H/1 * * * *')
    }

    stages{
        stage('Install Dependency'){
            steps{
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests'){
            steps{
                sh 'python3 -m pytest ./calci_test/test_app.py -v'
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