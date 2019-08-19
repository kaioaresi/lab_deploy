pipeline {
  agent any
  stages {
    stage('Env') {
      steps {
        input(message: 'Mensagem teste', id: 'TESTE', ok: 'OK', submitter: 'teste', submitterParameter: 'subpara')
      }
    }
  }
}