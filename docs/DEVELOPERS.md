
# 👨🏻‍💻 Developers

Thank you for considering embarking on this side quest. Let these tomes guide you on your journey. 🕯️

[*️⃣ 0. Requirements](#️⃣-0-requirements) \
[🔀 1. Fork](#🔀-1-fork) \
[⬇️ 2. Clone](#⬇️-2-clone) \
[➡️ 3. Settings](#➡️-3-settings) \
[▶️ 4. Start](#▶️-4-start) \
[↕️ 5. NPM](#↕️-5-npm) \
[⏩ 6. Build](#⏩-6-build) \
[🚹 7. User](#🚹-7-user) \
[↩️ 8. Logs](#↩️-8-logs) \
[↗️ 9. Open](#↗️-9-open) \
[🔄 10. Restart](#🔄-10-restart)


> [!TIP]
> Although this works in Docker Desktop, it may be easier to set up a dedicated VM and remotely connect with VSCode or equivalent. That way the environment it always set up ready to go without conflicts. Or use a local Ubuntu development PC with Docker if you're a baller.

## *️⃣ 0. Requirements

* 💫 A universe to exist in (or simulation)
* 🌐 The internet
* 🐋 [Docker](https://docs.docker.com/engine/install/)
* 🐳 [Docker Compose](https://docs.docker.com/compose/install/)
* 🏷️ [git](https://git-scm.com/downloads/linux)
* 🧠 Memory: ~8GB for development
* 🥔 CPU: ~2 Cores
* 💾 Disk: ~50GB when building images

## 🔀 1. Fork

> [!CAUTION]
> Please don't fork yet. We are in the process of detaching from the upstream mistio/mist-ce repo. We can't detach until there are no downstram forks. 

In the [https://github.com/mistcommunity/mist-ce](https://github.com/mistcommunity/mist-ce) repository on GitHub, click the Fork button to create a repository in your own personal GitHub account. 

## ⬇️ 2. Clone
Clone your fork to your development environment (replace with your username):

```shell
git clone --recursive https://github.com/{yourgithubusername}/mist-ce.git
cd mist-ce
```
By cloning the directory, there is also a `docker-compose.override.yml` file in the current directory in addition to `docker-compose.yml`. This is used to modify the configuration for development mode, which mounts the files in to the containers, overriding the files in the images.

## ➡️ 3. Settings

> [!NOTE]
> This will be simpler in the future

1. Copy `.env.template` to `.env`
2. Set the `IMG_TAG` to the version you wish to work on
3. Change the `IMG_REGISTRY` variable to `ghcr.io/mistcommunity` - unless you are building your own images, see below.
4. In `/api/settings/settings.py` set `JS_BUILD=false` - this tells the server to not use the source JavaScript files for live updating.



This will mount the checked out code into the containers and may take some time.

## ▶️ 4. Start

> [!TIP]
> If you are not interested in front-end development, you can comment out the UI sections within the `docker-compose.override.yml` file.

Now run 
```
docker compose up -d
```

## ↕️ 5. NPM
Install all front-end UI dependencies with the following commands:

```shell
docker compose exec ui npm install
```

If you want to build the UI bundles:

```shell
docker compose exec ui npm run build
```

As mentioned, when doing front-end development, it is usually more convenient to serve the source code instead of the bundles. To do that, edit `settings/settings.py` and set `JS_BUILD = False`. Restart the `api` container for the changes to take effect with:

```
./restart.sh api
```


## ⏩ 6. Build

**Optional**, if you want to build the images locally, and push to your own image repository (Docker Hub or GitHub), then modify the `.env` file.

`IMG_REGISTRY=ghcr.io/<GitHub user or organization name>` \
or \
`IMG_REGISTRY=<your dockerhub user name>` 

Change the version tag if you wish \
`IMG_TAG=4.20.69`

Then build the images:

```shell
docker compose build
docker compose up -d --wait
```

> [!NOTE]
> This will build all the Docker images and start them and it can take some time depending on performance of your computer. It is also expected that it will use quite a lot of disk space and RAM.

If you want to push to your repository, do:

```
docker compose push
```

## 🚹 7. User
```shell
docker compose exec api sh -c './bin/adduser --admin admin@example.com'
```

## ↩️ 8. Logs
To check on the progress and look for errors, tail the docker compose logs

```shell
docker compose logs -f
```

## ↗️ 9. Open 
If all looks good...
1. Open your browser and go to the Docker environment IP address (http port 80 only)
2. Login with the credentials you just created
3. ...
4. profit?

## 🔄 10. Restart

You will need to make the restart script executable:
```
sudo chmod +x restart.sh
```

When modifying the API, restart by running (from the root of the project):
```
./restart.sh api
```

When modifying the UI, sometimes you may need to restart it and clear your browser cache: 
```
./restart.sh ui
```

Or just restart everything
```
./restart.sh
```