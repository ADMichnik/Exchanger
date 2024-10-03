pipeline {
    agent { 
        label any
    }

    environment {
        API_KEY = credentials('api_key')
    }

    parameters {
        string(name: 'amount', defaultValue: '1000', description: 'Amount of currency')
        choice(name: 'base', choices: ['USD', 'EUR', 'PLN', 'GBP'])
        choice(name: 'target', choices: ['USD', 'EUR', 'PLN', 'GBP'])
    }

    stages {
        stage('Source') {
            steps {
                git url: 'https://github.com/ADMichnik/Exchanger.git', credentialsId: 'github-passwd', poll: false, branch: 'main'
            }
        }
        stage('Run script') {
            agent {
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                script {
                    sh 'python3 main.py -a ${amount} -b ${base} -t ${target}'
                }
            }
        }
    }
}
