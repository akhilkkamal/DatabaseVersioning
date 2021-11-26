pipeline {
    agent any
    environment {
    BRANCH_ENV = "${env.BRANCH_NAME}"
    }

    stages {
        stage('Setting up virtual env') {
            steps {
                sh '''#!/bin/bash
                    python3 -m venv .venv

                    source .venv/bin/activate
                    python3 -m pip install --upgrade pip
                    pip install -r requirement.txt
                    '''
            }
        }
        stage('Alembic Test') {
            when { anyOf { branch 'dev'; branch 'prd'} }
            steps {
                sh '''#!/bin/bash
                    source .venv/bin/activate
                    alembic -c ./alembic/alembic.ini -x parm_config=./alembic/config_${BRANCH_ENV}.ini upgrade head --sql
                    '''
            }
        }
        stage('Alembic Deploy') {
            when { anyOf { branch 'dev'; branch 'prd'} }
            steps {
                sh '''#!/bin/bash
                    source .venv/bin/activate
                    alembic -c ./alembic/alembic.ini -x parm_config=./alembic/config_${BRANCH_ENV}.ini upgrade head
                    '''
            }
        }
    }
}