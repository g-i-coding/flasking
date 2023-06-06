pipeline {
  agent {
    node {
      label 'docker'
    }

  }
  stages {
    stage('Git ') {
      steps {
        git(url: 'https://github.com/g-i-coding/flasking.git', branch: 'main')
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t celzey9/flask_app_new .'
      }
    }

    stage('Docker login') {
      steps {
        sh 'docker login -u celzey9 -p dckr_pat_tTA4FjEiYhs1LUgGN107sYYKnBI'
      }
    }

    stage('Docker Push') {
      steps {
        sh 'docker push celzey9/flask_app_new'
      }
    }

  }
}