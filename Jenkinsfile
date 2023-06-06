pipeline {

  enivronment {
    registry = "celzey9/flask_app_new"
    registryCredentials = "docker"
    cluster_name = "skillstorm"

  }
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

    stage('Build Stage') {
      steps {
        script {
          dockerImage - docker.build(registry)
        }
      }
    }

    stage('Deployment Stage') {
      steps {
        script {
          docker.withRegistry('', registryCredentials) {
            dockerImage.push()
          }
        }
      }
    }

  }
}