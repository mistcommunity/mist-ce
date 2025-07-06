<span id="top"></span>

# 🐋 Docker

Thank you for trying out mist, all feedback is welcome 📢

[*️⃣ 0. Requirements](#requirements) \
[⬇️ 1. Download](#download) \
[➡️ 2. Settings](#settings) \
[▶️ 4. Start](#start) \
[🚹 5. User](#user) \
[↗️ 6. Open](#open) \
[🔄 7. Options](#options)

> [!TIP]
> To avoid conflicts with existing containers and ports, it is recommended to use a dedicated VM with Docker and Docker Compose. Otherwise you can modify the docker-compose.yml to suite your specific environment.

> [!CAUTION]
> As per the Apache License 2.0, Mist Community Edition is provided as-is, without any guarantees or warranties. Use at your own risk. The contributors are not liable for data loss, security breaches, or financial loss.

<br>
<span id="requirements"></span>

## *️⃣ 0. Requirements

* 💫 A universe to exist in (or simulation)
* 🌐 The entirety of the internet
* 🤖 Human (optional) 
* 🐋 [Docker](https://docs.docker.com/engine/install/)
* 🐳 [Docker Compose](https://docs.docker.com/compose/install/)
* 🧠 Memory: 6GB-8GB
* 🥔 CPU: 2+ Cores
* 💾 Disk: ~40GB+ 

> The high memory usage is mostly due to Elasticsearch, we are considering a more lightweight alternative but would likely require significant re-development.

> The resource specifications are approximately what have been observed at initial setup and are the bare minimum

> [!NOTE]
> The original requirements specified "the latest stable Debian or Ubuntu" and "openssh-server". It should technically work on any Docker instance (x86/x64), however we have tested it at least runs on:
> - Debian (Bookworm 12 (stable)) + Docker (version 28.1.1, build 4eba377) + Docker Compose (version v2.35.1)
> - Alpine Linux (3.21.3) + Docker (27.3.1) + Docker Compose (2.31.0)
> - Docker Desktop (Windows)

> We aim to make this process simpler in the future.

<br>
<span id="download"></span>

## ⬇️ 1. Download

> The docker-compose.override.yml is for development use. See [DEVELOPERS.md](./DEVELOPERS.md)

1. Download or copy the [docker-compose.yml](../docker-compose.yml) and the [.env.template](../docker-compose.yml)
2. Rename **.env.template** to **.env**

<br>
<span id="settings"></span>

## ➡️ 2. Settings
1. Change `IMG_TAG` in the .env file to the desired version ([see tags](https://github.com/mistcommunity/mist-ce/tags)) or just `latest`
2. Set `IMG_REGISTRY` in .env to `ghcr.io/mistcommunity`

<br>
<span id="start"></span>

## ▶️ 4. Start
1. Run `docker compose up -d` or optionally run `docker compose pull` first to download the images
2. Then, run `docker-compose ps` or `docker stats` and verify that all containers are in the UP state, except the short-lived container elasticsearch-manage

<br>
<span id="user"></span>

## 🚹 5. User
1. Now, you need to create an admin user, run: 

```shell
docker compose exec api sh -c './bin/adduser --admin admin@example.com'
```

<br>
<span id="open"></span>

## ↗️ 6. Open 
If all looks good...
1. Open your browser and go to the Docker environment IP address (http port 80 only)
2. Login with the credentials you just created
3. ...
4. profit?

<br>
<span id="options"></span>

## 🔄 7. Options
> [!CAUTION]
> The following documentation is from the original README. It is outdated, over 2 years old, and will most certainly not work, yet. We will update it as we go.

#### Important configuration options
After the initial `docker-compose up -d`, you will see that a configuration file is created in `./settings/settings.py`. Edit this file to modify Mist's configuration.

Any changes to `./settings/settings.py` will take effect after a restart with:

```
docker-compose restart
```

##### URL
If running on anything other than `localhost`, you will need to set the `PORTAL_URI` setting in `./settings/settings.py`.

For example:

```
PORTAL_URI = "http://198.51.100.12"
```

##### Email
In some cases, such as user registration, forgotten passwords, user invitations etc., Mist needs to send emails. By default, Mist uses a mock mailer. To see emails sent by Mist, run:

```
docker-compose logs -f mailmock
```

If you wish to use an SMTP server, edit `./settings/settings.py` and modify `MAILER_SETTINGS`.

##### TLS
We strongly recommend using TLS. Assuming a certificate `cert.pem` and private key file `key.pem` in the same directory as the `docker-compose.yml` file, create a `docker-compose.override.yml` file with the following contents:

```yaml
version: '2.0'
services:
  nginx:
    volumes:
      - ./nginx-listen.conf:/etc/nginx/nginx-listen.conf:ro
      - ./cert.pem:/etc/nginx/cert.pem:ro
      - ./key.pem:/etc/nginx/key.pem:ro
    ports:
      - 443:443
```

Then, create a `nginx-listen.conf` in the directory of `docker-compose.yml`, with the following contents:

```
    listen 80;
    listen 443 ssl;
    server_name www.example.com;
    ssl_certificate     /etc/nginx/cert.pem;
    ssl_certificate_key /etc/nginx/key.pem;
    if ($scheme != "https") {
        rewrite ^ https://$host$uri permanent;
    }
```

Finally, update `PORTAL_URI` in Mist's settings and restart it.

##### Monitoring methods
Mist stores monitoring metrics in InfluxDB by default. Since Mist v4.6, it is possible to use VictoriaMetrics instead. You can configure that in `settings/settings.py`:

```
DEFAULT_MONITORING_METHOD = 'telegraf-victoriametrics'
```

Restart docker-compose for the changes to take effect and then run the respective migration script:

```
docker-compose exec api python migrations/0016-migrate-monitoring.py
```

The above script will update all monitored machines to use the configured monitoring method. It will also update all rules on metrics to use the appropriate query format. However, this **will not** migrate old monitoring data to the new time series database.

#### Upgrade
To upgrade to a new Mist version:

1. Stop your current Mist by running `docker-compose down`.
2. Download the `docker-compose.yml` file of the latest release and place it
in the same directory as before. This way the new installation will use the
same Docker volumes.
3. Run `docker-compose up -d` to bring up the new version.
4. Check that everything is in order by running `docker-compose ps`.

#### Backup
Mist can automatically take and store backups in an S3-compatible bucket. To set this up, first create a bucket on your S3 provider, e.g. AWS, MinIO, etc.

Then, go to `settings/setting.py` and edit the following part accordingly:

```python
BACKUP_INTERVAL = 24  # hours between each backup
BACKUP = {
    'host': '',  # eg s3.amazonaws.com
    'key': '',
    'secret': '',
    'bucket': '',
    'gpg': {
        'recipient': '',
        'public': '',
        'private': '',
    }
}
```

Providing a GPG key is optional but strongly recommended. If you provide it, your backups will be encrypted before getting uploaded to your bucket.

Mist also offers a set of manual commands for backing up, listing backups and restoring backups:

```
docker-compose exec api ./bin/backup
docker-compose exec api ./bin/list-backups
docker-compose exec api ./bin/restore {{myBackupName}}
```

Backups on time series data stored on VictoriaMetrics will be incremental by default. To perform a full backup, use the `--no-incremental` flag:

```
docker-compose exec api ./bin/backup --db victoria --no-incremental
```

Finally, please keep in mind that backups include MongoDB, InfluxDB & VictoriaMetrics data. Mist logs are stored in Elasticsearch. If you would like to back up these as well, please check out [this doc](https://www.elastic.co/guide/en/elasticsearch/reference/current/backup-cluster.html).

#### Staging version
If you want to install the latest bleeding edge build of Mist, run the following:

```
mkdir mist-ce && cd mist-ce && echo 'MIST_TAG=staging' > .env
wget https://raw.githubusercontent.com/mistio/mist-ce/staging/docker-compose.yml
docker-compose up -d
```