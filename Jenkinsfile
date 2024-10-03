pipeline {
    agent any

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
                git url: 'https://github.com/ADMichnik/Exchanger.git', poll: false, branch: 'main'
            }
        }
        stage('Run script') {
            steps {
                script {
                    docker.image('python:3.9-slim').inside {
                        sh 'python main.py -a ${amount} -b ${base} -t ${target}'
                    }
                }
            }
        }
    }
}
