pipeline {
  agent any
  stages {
    stage('Env') {
      steps {
        waitUntil() {
          input(message: 'Digite o env', id: 'ID', ok: 'confirma', submitter: 'submitter', submitterParameter: 'submitterParameter')
        }

      }
    }
  }
}