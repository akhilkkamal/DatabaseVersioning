pipeline {
    agent any

    stages {
        stage('Setting up virtual env') {
            steps {
                sh '''#!/bin/bash
                    python3 -m venv .venv

                    source .venv/bin/activate
                    python3 -m pip install --upgrade pip
                    pwd
                    ls
                    pip install -r requirement.txt
                    '''
            }
        }
        stage('Alembic Test') {
            steps {
                sh '''#!/bin/bash
                    alembic -c ./alembic.ini -x parm_config=./config.ini upgrade head --sql
                    '''
            }
        }
        stage('Alembic Deploy') {
            steps {
                sh '''#!/bin/bash
                    alembic -c ./alembic.ini -x parm_config=./config.ini upgrade head
                    '''
            }
        }
    }
}