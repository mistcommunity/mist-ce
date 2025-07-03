# 🗺️ Roadmap
> [!IMPORTANT] 
> This roadmap is a continuous work in progress, the versions and features here are a very rough outline and are subject to change. See [CHANGELOG](./CHANGELOG.md) for previous versions


## Versions
- [CHANGELOG](./CHANGELOG.md)
- [v4.8.x - Current](#v48x---current)
- [v4.9.x - v4.x.x](#v49x---v4xx)
- [v5.0.0](#v500)
- [v6.0.x](#v60x)
- [v7.0.x](#v70x)
- [v8.0.x](#v80x)
- [Meta](#meta)

```
✅ Merged and commit version tag
🎬 Staging
🔀 PR Pending
⏳ In Progress 
✨ New 
```

## v4.8.x - Current
> Initialize community, simplify, remove branding and start docs

| Version |<div style="width:80px">Category</div> | Status | Description                                                     | Issue
|---------|-------------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| v4.8.0  | 🚀Simplify |🎬     | Monorepo, dependency updates, GH Actions, other fixes           | [#1](https://github.com/mistcommunity/mist-ce/issues/1)
| v4.8.1  | 🚀Simplify |🎬     | Remove landing app with blog / pricing / marketing etc.         | [#25](https://github.com/mistcommunity/mist-ce/issues/25)
| v4.8.2  | 📖Docs     |⏳     | Update readme, create roadmap, update changelog, branches audit | [#17](https://github.com/mistcommunity/mist-ce/issues/17)
| v4.8.3  | 📖Docs     |✨     | Hugo docs for gh-pages and self-hosted site                     | [#17](https://github.com/mistcommunity/mist-ce/issues/17)
| v4.8.4  | 🚀Simplify |✨     | Remove proprietary branding, create new logo                    | [#11](https://github.com/mistcommunity/mist-ce/issues/11)
| v4.8.5  | 🚀Simplify |✨     | Remove external links and tracking                              | [#5](https://github.com/mistcommunity/mist-ce/issues/5)
| v4.8.6  | 🚀Simplify |✨     | Remove stripe and payments                                      | [#24](https://github.com/mistcommunity/mist-ce/issues/24)
| v4.8.7  | 🚀Simplify |✨     | Simplify & consolidate configuration / environment settings     | [#33](https://github.com/mistcommunity/mist-ce/issues/33)
| v4.8.8  | 🚀Simplify |✨     | Simplify logging (is Elasticsearch/Logstash/Kibana necessary?)  | [#7](https://github.com/mistcommunity/mist-ce/issues/7)
| v4.8.9  | 🚀Simplify |✨     | Fix & simplify vault / secrets                                  | 
| v4.8.10 | 🛠️Fix      |✨     | Simplify / fix swagger                                          | [#14](https://github.com/mistcommunity/mist-ce/issues/14)
| v4.8.11 | 🛠️Fix      |✨     | Update / sort out Traefik                                       | [#8](https://github.com/mistcommunity/mist-ce/issues/8)
| v4.8.12 | 🚀Simplify |✨     | Victoria metrics / InfluxDB / Other metrics DB                  | [#16](https://github.com/mistcommunity/mist-ce/issues/16)
| v4.8.13 | 🚀Simplify |✨     | Fix / remove / change RabbitMQ                                  | [#18](https://github.com/mistcommunity/mist-ce/issues/18)
| v4.8.14 | 🚀Simplify |✨     | Temporarily remove network features                             | [#12](https://github.com/mistcommunity/mist-ce/issues/12)
| v4.8.15 | 🚀Simplify |✨     | Temporarily remove IBM cloud                                    | [#19](https://github.com/mistcommunity/mist-ce/issues/19)
| v4.8.16 | 🚀Simplify |✨     | Remove Gocky (InfluxDB loadbalancer)                            | 


## v4.9.x - v4.x.x
> Focus: Minimum viable VM compute support for major cloud/hypervisor platforms

| Version  | Category  | Status | Description                                                     | Issue
|----------|-----------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| v4.9.x   | 💡Feature |✨     | Nutanix                                                         | [#2](https://github.com/mistcommunity/mist-ce/issues/2)
| v4.10.x  | 🛠️Fix     |✨     | AWS                                                             | 
| v4.11.x  | 🛠️Fix     |✨     | Azure                                                           | 
| v4.12.x  | 🛠️Fix     |✨     | GCP                                                             | 
| v4.13.x  | 🛠️Fix     |✨     | VMware                                                          | 
| v4.14.x  | 🛠️Fix     |✨     | Vultr                                                           | 
| v4.15.x  | 🛠️Fix     |✨     | DigitalOcean                                                    | 
| v4.16.x  | 🛠️Fix     |✨     | Linode                                                          | 
| v4.17.x  | 💡Feature |✨     | Proxmox VE                                                      | 


## v5.x.x
> Full enterprise features in community edition

| Version  | Category   | Status | Description                                                     | Issue
|----------|------------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| v5.0.x   | 🚀Simplify |✨     | Fully up to date with legacy branches (v5)                      | 
| v5.1.x   | 🛠️Fix      |✨     | RBAC working                                                    | [#3](https://github.com/mistcommunity/mist-ce/issues/3)
| v5.2.x   | 🛠️Fix      |✨     | Account management (reset passwords, create accounts etc)       |
| v5.3.x   | 🛠️Fix      |✨     | Re-introduce SSO                                                | [#9](https://github.com/mistcommunity/mist-ce/issues/9)
| v5.4.x   | 🛠️Fix      |✨     | Tests                                                           | 
| v5.5.x   | 🛠️Fix      |✨     | Other legacy enterprise features                                | 
| v5.6.x   | 🛠️Fix      |✨     | Self monitoring (VM / Docker)                                   | 
| v5.7.x   | 🚀Simplify |✨     | API v1/v2 merged                                                | 


## v6.x.x
> UI Update

| Version  | Category   | Status | Description                                                     | Issue
|----------|------------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| v6.0.x   | 🔄Update   |✨     | Update UI web components and node modules                       | 
| v6.1.x   | 🔄Update   |✨     | Migrate to Lit web components                                   | 
| v6.2.x   | 🛠️Fix      |✨     | Themes                                                          | 


## v7.x.x
> Additional clouds and functions

| Version  | Category  | Status | Description                                                     | Issue
|----------|-----------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| v7.0.x   | 💡Feature |✨     | Hetzner                                                         | 
| v7.1.x   | 💡Feature |✨     | Scaleway                                                        | 
| v7.2.x   | 💡Feature |✨     | Bare metal                                                      | 
| v7.3.x   | 🛠️Fix     |✨     | Generic Linux VM                                                | 
| v7.4.x   | 🛠️Fix     |✨     | Docker                                                          | 
| v7.5.x   | 🛠️Fix     |✨     | Kubernetes                                                      | 
| v7.6.x   | 💡Feature |✨     | DNS                                                             | 
| v7.7.x   | 💡Feature |✨     | Unraid                                                          | 
| v7.8.x   | 💡Feature |✨     | Custom images to upload to clouds                               | [#21](https://github.com/mistcommunity/mist-ce/issues/21)
| v7.9.x   | 🛠️Fix     |✨     | Re-introduce networks                                           | 


## v8.0.x
> CI/CD automation (infrastructure as code)

| Version  | Category  | Status | Description                                                     | Issue
|----------|-----------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| v8.0.x   | 💡Feature |✨     | CI/CD deployments                                               | 
| v8.1.x   | 💡Feature |✨     | Terraform?                                                      | 
| v8.2.x   | 💡Feature |✨     | Ansible?                                                        | 


## v9.0.x
> Automated application deployment

| Version  | Category  | Status | Description                                                     | Issue
|----------|-----------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| v9.0.x   | 💡Feature |✨     | Deploy predefined apps, similar to [elestio](https://elest.io/) | 
| v9.1.x   | 💡Feature |✨     | Integrate with Portainer app store                              | 
| v9.2.x   | 💡Feature |✨     | Integrate with Unraid app store                                 | 
| v9.3.x   | 💡Feature |✨     | Integrate with CasaOS app store                                 | 


## v10.0.x
> Framework update

| Version  | Category   | Status | Description                                                     | Issue
|----------|------------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| v10.0.x  | 💡Feature |✨     | Migrate to a new UI framework (Angular/React/Next/?)            | [#29](https://github.com/mistcommunity/mist-ce/discussions/29)
| v10.1.x  | 💡Feature |✨     | New backend if required (Supabase or something else?)           | 


## Meta
> Ongoing changes

| Version  | Category    | Status | Description                                                     | Issue
|----------|-------------|--------|-----------------------------------------------------------------|----------------------------------------------------------
| All      | 🧪Testing  |✨     | Test features then update [FEATURES](./FEATURES.md)             | [#1](https://github.com/mistcommunity/mist-ce/issues/1)
| All      | 📖Docs     |✨     | Update Hugo docs site                                           | [#17](https://github.com/mistcommunity/mist-ce/issues/17)
| All      | 📖Docs     |✨     | Update roadmap                                                  | [#17](https://github.com/mistcommunity/mist-ce/issues/17)
| All      | 📖Docs     |✨     | Update changelog                                                | [#17](https://github.com/mistcommunity/mist-ce/issues/17)
| All      | 🚀Simplify |✨     | Compare, merge and delete legacy branches                       | [#27](https://github.com/mistcommunity/mist-ce/issues/27)
| All      | 🚀Simplify |✨     | Detach from upstream                                            | [#31](https://github.com/mistcommunity/mist-ce/issues/31)
