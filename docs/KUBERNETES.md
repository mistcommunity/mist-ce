# <img src="./assets/providers/provider-kubernetes.png" height="28"/> Kubernetes
> [!CAUTION]
> These are legacy instructions from the original project. Kubernetes has not been tested.

To get started, you will need:

1. A working and up-to-date Kubernetes cluster, able to allocate 8 CPUs and 16GB of RAM to Mist. 
3. Access rights to run Helm on your cluster.

Run the following commands to install Mist:

```
helm repo add mist https://dl.mist.io/charts
helm repo update
helm install mist-ce mist/mist-ce
```

Finally, follow the on-screen instructions after the installation is completed to configure an ingress IP and create the required Mist admin user.

Linode and Vultr users can find detailed installation videos in the respective, official YouTube channels.

#### Important configuration options

##### Domain and TLS

The quick installation method described above does not set up TLS. This is done in order to keep things simple and get you to test Mist quickly. However, we strongly recommend using TLS. This requires a domain for your Mist installation.

First, configure your DNS to point to your cluster's IP.

If you want to issue a new certificate, configure the cluster issuer that will be used, e.g.:

```
helm install mist-ce mist/mist-ce --set http.host=foo.bar.com  \
  --set http.tlsClusterIssuer=letsencrypt-prod \
  --set http.tlsSecret=secretName
```

For instructions on how to install and configure cert-manager read the docs [here](https://cert-manager.io/docs/installation/).

If you have configured a TLS certificate for this hostname as a Kubernetes secret, you should use the `http.tlsSecret` option, e.g.:

```
helm install mist-ce mist/mist-ce --set http.host=foo.bar.com \
  --set http.tlsSecret=secretName
```

##### Email

In some cases, such as user registration, forgotten passwords, user invitations etc., Mist needs to send emails. By default, Mist uses a mock mailer.

To see emails sent by Mist, get the relevant pod name:

```
kubectl get pods -l app=mailmock
```

Now, view the logs of this pod, e.g.: 

```
kubectl logs -f mailmock-pod-name
```

If you wish to use an SMTP server, do something like this:

```
helm install mist-ce mist/mist-ce --set smtp.host=smtp.foo.bar.com \
  --set smtp.username=foo
  --set smtp.password=bar
  --set smtp.port=25
  --set smtp.tls=false
  --set smtp.starttls=true
```

##### External Docker host

Mist's orchestration plugin needs to deploy Docker containers. By default, Mist deploys an in-cluster `dockerhost` pod in privileged mode.

To use an external Docker host, set the following:

```
helm install mist-ce mist/mist-ce --set docker.host=dockerIP \
  --set docker.port=dockerPort \
  --set docker.key=TLSKey \
  --set docker.cert=TLSCert \
  --set docker.ca=TLSCACert
```

#### All configuration options

To review and customize all available configuration options:

1. Export the default chart values.
```
helm show values mist/mist-ce > values.yaml
```
2. Edit the exported `values.yaml`.
3. Run `helm install` with `values.yaml` as input.
```
helm install mist-ce mist/mist-ce -f values.yaml
```

The following table lists all the configurable parameters in Mist's Helm chart and their default values.

|            Parameter                       |              Description                                                           |            Default                |
| ------------------------------------------ | ---------------------------------------------------------------------------------- | --------------------------------- |
| `http.host`                                | FQDN or IP of Mist installation.                                                    | `localhost`                       |
| `http.http2`                               | Use HTTP/2.                                                                         | `false`                           |
| `http.tlsSecret`                           | Kubernetes secret containing the `tls.crt` and `tls.key` data.                         | `''`                              |
| `http.tlsHosts`                            | Array of TLS hosts for ingress record.                                              | `[]`                              |
| `http.tlsAnnotations`                      |                                                                                    | `{}`                              |
| `http.tlsClusterIssuer`                    | TLS cluster issuer.                                                              | `''`                              |
| `smtp.host`                                | SMTP mail server address.                                                           | `''`                              |
| `smtp.port`                                | SMTP port.                                                                      | `8025`                            |
| `smtp.username`                            | SMTP username.                                                                      | `''`                              |
| `smtp.password`                            | SMTP password.                                                                     | `''`                              |
| `smtp.tls`                                 | Use TLS with SMTP.                                                                  | `false`                           |
| `smtp.starttls`                            | Send the starttls command. Typically, it is not used with `smtp.tls=true`.    | `false`                           |
| `portalAdmin.enabled`                      | Create a Mist admin user upon chart installation.                    | `true`                            |
| `portalAdmin.organization`                 | Mist organization name.                                                              | `example.com`                     |
| `portalAdmin.mail`                         | Mist admin's email address.                                                          | `admin@example.com`               |
| `portalAdmin.password`                     | Mist admin's password.                                                              | `example.com`                     |
| `portalAdmin.createApiToken`               | Create an API token upon chart installation.                                         | `true`                            |
| `docker.deploy`                            | Deploy a dockerhost pod in-cluster. The pod will run in privileged mode.           | `true`                            |
| `docker.host`                              | External Docker host address.                                                        | `''`                              |
| `docker.port`                              | External Docker host port.                                                          | `2375`                            |
| `docker.key`                               | External Docker host SSL private key.                                            | `''`                              |
| `docker.cert`                              | External Docker host SSL certificate.                                            | `''`                              |
| `docker.ca`                                | External Docker host CA certificate.                                             | `''`                              |
| `vault.address`                            | HashiCorp Vault address to use.                                                                      | `http://vault:8200`               |
| `vault.token`                              | Authentication token for HashiCorp Vault.                                                     | `''`                              |
| `vault.roleId`                             | HashiCorp Vault `RoleID`.                                                                   | `''`                              |
| `vault.secretId`                           | HashiCorp Vault `SecretID`.                                                                 | `''`                              |
| `vault.secret_engine_path`                 |                                                                                    | `{}`                              |
| `vault.clouds_path`                        | Default HashiCorp Vault path for Mist cloud credentials.                                       | `mist/clouds/`                    |
| `vault.keys_path`                          | Default HashiCorp Vault path for Mist key credentials.                                         | `mist/keys`                       |
| `elasticsearch.host`                       | ElasticSearch host.                                                             | `''`                              |
| `elasticsearch.port`                       | ElasticSearch port.                                                            | `9200`                            |
| `elasticsearch.username`                   | Username for ElasticSearch with basic auth.                                         | `''`                              |
| `elasticsearch.password`                   | Password for ElasticSearch with basic auth.                                        | `''`                              |
| `elasticsearch.tls`                        | Connect to ElasticSearch using TLS.                                                 | `false`                           |
| `elasticsearch.verifyCerts`                | Verify ElasticSearch TLS.                                                       | `false`                           |
| `influxdb.host`                            | InfluxDB host.                                                                  | `''`                              |
| `influxdb.port`                            | Verify InfluxDB TLS.                                                       | `8086`                            |
| `influxdb.db`                              | InfluxDB database to use.                                                       | `telegraf`                        |
| `influxdb.monitoring`                      |                                                                                    | `true`                            |
| `influxdb.storageSize`                     | Size of the InfluxDB pvc.                                                       | `1024Mi`                          |
| `victoriametrics.enabled`                  |                                                                                    | `true`                            |
| `victoriametrics.deploy`                   | Deploy a VictoriaMetrics cluster.                                                  | `true`                            |
| `victoriametrics.readEndpoint`             | External VictoriaMetrics cluster read endpoint.                                    | `''`                              |
| `victoriametrics.writeEndpoint`            | External VictoriaMetrics cluster write endpoint.                                   | `''`                              |
| `victoriametrics.vmstorage.persistentVolume.storageClass` | StorageClass of the VictoriaMetrics pvc.                         | `standard`                        |
| `victoriametrics.vmstorage.persistentVolume.size` | Size of the VictoriaMetrics pvc.                                         | `1024Mi`                          |
| `rabbitmq.deploy`                          | Deploy RabbitMQ cluster.                                                          | `true`                            |
| `rabbitmq.replicaCount`                    | RabbitMQ replicas to deploy.                                              | `1`                               |
| `rabbitmq.replicationFactor`               | Default replication factor for queues.                                              | `1`                               |
| `rabbitmq.auth.username`                   | RabbitMQ username.                                                                  | `guest`                           |
| `rabbitmq.auth.password`                   | RabbitMQ password.                                                                  | `guest`                           |
| `rabbitmq.auth.erlangCookie`               | Erlang cookie to determine whether nodes are allowed to communicate with each other.| `guest`                           |
| `rabbitmqExternal.host`                    | External RabbitMQ address. Only used when `rabbitmq.deploy` is `false`.              | `''`                              |
| `rabbitmqExternal.port`                    | External RabbitMQ port.                                                             | `5672`                            |
| `rabbitmqExternal.username`                | External RabbitMQ username.                                                         | `guest`                           |
| `rabbitmqExternal.password`                | External RabbitMQ password.                                                         | `guest`                           |
| `mongodb.deploy`                           | Deploy MongoDB cluster.                                                           | `true`                            |
| `mongodb.host`                             | External MongoDB address. Only used when `mongodb.deploy` is `false`.                | `''`                              |
| `mongodb.port`                             | External MongoDB port.                                                              | `27017`                           |
| `monitoring.defaultMethod`                 | Available options: `telegraf-victoriametrics` and `telegraf-influxdb`                 | `telegraf-influxdb`               |
| `auth.email.signup`                        | Allow signups with email & password.                                                  | `false`                           |
| `auth.email.signin`                        | Allow signins with email & password.                                                  | `true`                            |
| `auth.google.signup`                       | Allow signups with Google oAuth.                                                    | `false`                           |
| `auth.google.signin`                       | Allow signins with Google oAuth.                                                    | `false`                           |
| `auth.google.key`                          | Google oAuth client ID.                                                     | `''`                              |
| `auth.google.secret`                       | Google oAuth client Secret.                                                  | `''`                              |
| `auth.github.signup`                       | Allow signups with Github oAuth.                                                    | `false`                           |
| `auth.github.signin`                       | Allow signins with Github oAuth.                                                    | `false`                           |
| `auth.github.key`                          | Github oAuth client ID.                                                    | `''`                              |
| `auth.github.secret`                       | Github oAuth client secret.                                                  | `''`                              |
| `backup.key`                               | AWS API key.                                                                        | `''`                              |
| `backup.secret`                            | AWS API secret.                                                                     | `''`                              |
| `backup.bucket`                            | AWS S3 bucket name used to store backups.                                           | `''`                              |
| `backup.region`                            | AWS S3 bucket region.                                        | `''`                              |
| `backup.gpg.recipient`                     | Email recipient of the encrypted backup.                                        | `''`                              |
| `backup.gpg.public`                        | GPG public key.                                                                 | `''`                              |
| `githubBotToken`                           |                                                                                    | `''`                              |
| `deployment.gocky.replicas`                | Replicas in Gocky deployment.                                                      | `1`                               |
| `deployment.api.replicas`                  | Replicas in API server deployment.                                                        | `2`                               |
| `deployment.sockjs.replicas`               | Replicas in sockjs deployment                                                     | `1`                               |
| `deployment.ui.replicas`                   | Replicas in Mist UI deployment.                                                         | `1`                               |
| `deployment.nginx.replicas`                | Replicas in NGINX deployment.                                                      | `1`                               |
| `deployment.landing.replicas`              | Replicas in Mist's landing webpage deployment.                                                    | `1`                               |
| `deployment.dramatiq.dramatiq.enabled`     | Enable Dramatiq consumers for all queues.                                           | `true`                            |
| `deployment.dramatiq.dramatiq.replicas`    |                                                                                    | `2`                               |
| `deployment.dramatiq.default.enabled`      | Enable Dramatiq consumers for `default` queue.                                      | `false`                           |
| `deployment.dramatiq.default.replicas`     |                                                                                    | `1`                               |
| `deployment.dramatiq.provisioning.enabled` | Enable Dramatiq consumers for `dramatiq_provisioning` queue.                        | `false`                           |
| `deployment.dramatiq.provisioning.replicas`|                                                                                    | `1`                               |
| `deployment.dramatiq.polling.enabled`      | Enable Dramatiq consumers for `dramatiq_polling` queue.                             | `false`                           |
| `deployment.dramatiq.polling.replicas`     |                                                                                    | `1`                               |
| `deployment.dramatiq.machines.enabled`     | Enable Dramatiq consumers for `dramatiq_machines` queue.                            | `false`                           |
| `deployment.dramatiq.machines.replicas`    |                                                                                    | `1`                               |
| `deployment.dramatiq.clusters.enabled`     | Enable Dramatiq consumers for `dramatiq_clusters` queue.                            | `false`                           |
| `deployment.dramatiq.clusters.replicas`    |                                                                                    | `1`                               |
| `deployment.dramatiq.networks.enabled`     | Enable Dramatiq consumers for `dramatiq_networks` queue.                            | `false`                           |
| `deployment.dramatiq.networks.replicas`    |                                                                                    | `1`                               |
| `deployment.dramatiq.zones.enabled`        | Enable Dramatiq consumers for `dramatiq_zones` queue.                               | `false`                           |
| `deployment.dramatiq.zones.replicas`       |                                                                                    | `1`                               |
| `deployment.dramatiq.volumes.enabled`      | Enable Dramatiq consumers for `dramatiq_volumes` queue.                             | `false`                           |
| `deployment.dramatiq.volumes.replicas`     |                                                                                    | `1`                               |
| `deployment.dramatiq.buckets.enabled`      | Enable Dramatiq consumers for `dramatiq_buckets` queue.                             | `false`                           |
| `deployment.dramatiq.buckets.replicas`     |                                                                                    | `1`                               |
| `deployment.dramatiq.mappings.enabled`     | Enable Dramatiq consumers for `dramatiq_mappings` and `dramatiq_sessions` queues.      | `false`                           |
| `deployment.dramatiq.mappings.replicas`    |                                                                                    | `1`                               |
| `deployment.dramatiq.scripts.enabled`      | Enable Dramatiq consumers for `dramatiq_scripts` queue.                             | `false`                           |
| `deployment.dramatiq.scripts.replicas`     |                                                                                    | `1`                               |
| `deployment.dramatiq.probe.enabled`        | Enable Dramatiq consumers for `dramatiq_ssh_probe` queue.                           | `false`                           |
| `deployment.dramatiq.probe.replicas`       |                                                                                    | `1`                               |
| `deployment.dramatiq.ping.enabled`         | Enable Dramatiq consumers for `dramatiq_ping_probe` queue.                          | `false`                           |
| `deployment.dramatiq.ping.replicas`        |                                                                                    | `1`                               |
| `deployment.dramatiq.rules.enabled`        | Enable Dramatiq consumers for `dramatiq_rules` queue.                               | `false`                           |
| `deployment.dramatiq.rules.replicas`       |                                                                                    | `1`                               |
| `deployment.dramatiq.schedules.enabled`    | Enable Dramatiq consumers for `dramatiq_schedules` queue.                           | `false`                           |
| `deployment.dramatiq.schedules.replicas`   |                                                                                    | `1`                               |
| `deployment.scheduler.scheduler.enabled`   | Enable scheduler for all polling schedules.                                         | `true`                            |
| `deployment.scheduler.scheduler.replicas`  |                                                                                    | `1`                               |
| `deployment.scheduler.builtin.enabled`     | Enable scheduler for `builtin` schedules.                                           | `false`                           |
| `deployment.scheduler.builtin.replicas`    |                                                                                    | `1`                               |
| `deployment.scheduler.user.enabled`        | Enable scheduler for `user` schedules.                                              | `false`                           |
| `deployment.scheduler.user.replicas`       |                                                                                    | `1`                               |
| `deployment.scheduler.polling.enabled`     | Enable scheduler for `polling` schedules.                                           | `false`                           |
| `deployment.scheduler.polling.replicas`    |                                                                                    | `1`                               |
| `deployment.scheduler.rules.enabled`       | Enable scheduler for `rules` schedules.                                             | `false`                           |
| `deployment.scheduler.rules.replicas`      |                                                                                    | `1`                               |
