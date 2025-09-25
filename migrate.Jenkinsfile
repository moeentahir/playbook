pipeline {
    agent any

    parameters {
        string(name: 'source_cluster', defaultValue: '', description: 'Source cluster name')
        string(name: 'target_cluster', defaultValue: '', description: 'Target cluster name')
        text(name: 'namespaces', defaultValue: '', description: 'Comma-separated list of namespaces')
    }

    stages {
        stage('Process Namespaces') {
            steps {
                script {
                    // Split namespaces by comma or newline and trim spaces
                    def nsList = params.namespaces
                        .split(/[\n,]+/)
                        .collect { it.trim() }
                        .findAll { it } // remove empty entries

                    echo "Namespaces to process: ${nsList}"

                    nsList.each { ns ->
                        echo "Triggering pipeline for namespace: ${ns}"

                        build job: 'other-pipeline', // replace with actual job name
                              parameters: [
                                  string(name: 'source_cluster', value: params.source_cluster),
                                  string(name: 'target_cluster', value: params.target_cluster),
                                  string(name: 'namespace', value: ns)
                              ],
                              wait: false // set true if you want to wait for completion
                    }
                }
            }
        }
    }
}
