pipeline {
  environment {
    registry = "celzey9/flask_app_new"
    registryCredentials = "docker"
    cluster_name = "skillstorm"
    namespace = "celzey9"
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
          dockerImage = docker.build(registry)
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
    stage('Kubernetes') {
      steps {
        script {
          withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-credentials', secretKeyVariable: "AWS_SECRET_ACCESS_KEY")]) {
            sh "aws eks --region us-east-1 update-kubeconfig --name ${cluster_name}"
            script {
              try {
                sh "kubectl create namespace ${namespace}"

              }
              catch (Exception e) {
                echo "Error / namespace already created"
              }
            }
            sh "kubectl apply -f deployment.yaml -n ${namespace}"
            sh "kubectl -n ${namespace} rollout restart deployment celzeyflask"
            }
        }
      }
    }
  }
}