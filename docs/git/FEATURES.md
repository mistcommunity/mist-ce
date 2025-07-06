# ✨ Features
> [!NOTE]
> Due to outdated libraries and minimal access to services, the clouds, functions and methods need to be verified.

✅: Functionality confirmed working \
⚠️: Partially working or known issues \
❌: Not supported or broken \
❓: Unknown or unverified \
✨: New feature


## Historically advertised features

| Tier  | Feature                                                                                                                              | Status
|-------|--------------------------------------------------------------------------------------------------------------------------------------|--------
| CE    | Support for more than 20 infrastructure technologies.                                                                                | ❓
| CE    | Instant visibility of all the available resources across clouds, grouped by tags.                                                    | ❓
| CE    |  Instant reporting/estimation of the current infrastructure costs.                                                                   | ❓
| EE/HS | Compare current & past costs, correlate with usage, provide right-sizing recommendations.                                            | ❓
| CE    | Provision new resources on any cloud including machines, clusters, volumes, networks, zones and DNS records.                         | ❓
| CE    | Deploy and scale Kubernetes clusters on any supported cloud.                                                                         | ❓
| CE    | Perform lifecycle actions on existing resources, e.g. stop, start, reboot, resize, destroy, etc.                                     | ❓
| CE    | Upload scripts and run them on any machine while enforcing audit logging and centralized control of SSH keys.                        | ❓
| CE    | SSH command shell on any machine within the browser or through the CLI, enforcing audit logging and centralized control of SSH keys. | ❓
| CE    |Instant audit logging for all actions performed through Mist or detected through continuous polling.                                  | ❓
| CE    |Monitor machines, display real time system & custom metrics and store them for long term access.                                      | ❓
| CE    |Set rules on metrics or logs that trigger notifications, webhooks, scripts or lifecycle actions.                                      | ❓
| CE    | Set schedules that trigger scripts or machine lifecycle actions.                                                                     | ❓
| EE/HS |Set fine-grained access control policies per team, tag, resource and/or action.                                                       | ❓
| EE/HS |Set governance constraints: e.g. quotas on cost per user/team, required expiration dates.                                             | ❓
| EE/HS |Upload infrastructure templates that may describe complex deployments and workflows.                                                  | ❓



## Providers

|                                                       | Provider               | Type          | Status | Issue       
|-------------------------------------------------------|------------------------|---------------|--------|-------
|![aws](./assets/providers/aws.svg)                     | Amazon Web Services    | Public Cloud  | ❓    |
|![azu](./assets/providers/provider-azure.png)          | Microsoft Azure        | Public Cloud  | ❓    |
|![gce](./assets/providers/provider-gce.png)            | Google Cloud           | Public Cloud  | ❓    |
|![ali](./assets/providers/provider-aliyunecs.png)      | Alibaba Cloud          | Public Cloud  | ❓    |
|![ibm](./assets/providers/provider-ibm.png)            | IBM Cloud              | Public Cloud  | ❓    |
|![doc](./assets/providers/provider-digitalocean.png)   | Digital Ocean          | Public Cloud  | ❓    |
|![equ](./assets/providers/provider-equinixmetal.png)   | Equinix Metal          | Public Cloud  | ❓    |
|![lin](./assets/providers/provider-linode.png)         | Linode                 | Public Cloud  | ⚠️    |
|![rac](./assets/providers/provider-rackspace.png)      | Rackspace              | Public Cloud  | ❓    |
|![vul](./assets/providers/provider-vultr.png)          | Vultr                  | Public Cloud  | ❓    |
|![max](./assets/providers/provider-maxihost.png)       | Maxihost               | Public Cloud  | ❓    |
|![vex](./assets/providers/provider-vexxhost.png)       | Vexxhost               | Public Cloud  | ❓    |
|![csg](./assets/providers/provider-cloudsigma.png)     | CloudSigma             | Public Cloud  | ❓    |
|![ost](./assets/providers/provider-openstack.png)      | OpenStack              | Private Cloud | ❓    |
|![ona](./assets/providers/provider-onapp.png)          | OnApp                  | Private Cloud | ❓    |
|![vmw](./assets/providers/provider-vsphere.png)        | VMWare vSphere         | Private Cloud | ❓    |
|![kvm](./assets/providers/provider-libvirt.png)        | KVM                    | Private Cloud | ❓    |
|![pro](./assets/providers/provider-proxmox.png)        | Proxmox                | Private Cloud | ❌    |
|![nut](./assets/providers/provider-nutanix.png)        | Nutanix                | Private Cloud | ❌    | [#2](https://github.com/mistcommunity/mist-ce/issues/2)
|![hyp](./assets/providers/provider-hyperv.png)         | Hyper-V                | Private Cloud | ❌    |
|![unr](./assets/providers/provider-unraid.png)         | UnRaid                 | Private Cloud | ❌    |


## OS

|                                                       | Provider               | Type          | Status | Issue       
|-------------------------------------------------------|------------------------|---------------|--------|-------
|<img src="./assets/os/windows.svg" height="44"/>       | Windows                | OS            | ❓    |
|<img src="./assets/os/alpine.svg" height="44"/>        | Alpine                 | OS            | ❓    |
|<img src="./assets/os/ubuntu.svg" height="44"/>        | Ubuntu                 | OS            | ❓    |
|<img src="./assets/os/linux.svg" height="44"/>         | General Linux          | OS            | ❓    |
|<img src="./assets/os/arch.svg" height="44"/>          | Arch                   | OS            | ❓    |
|<img src="./assets/os/suse.svg" height="44"/>          | Suse                   | OS            | ❓    |


## Containerization

|                                                       | Provider               | Type          | Status | Issue       
|-------------------------------------------------------|------------------------|---------------|--------|-------
|![kub](./assets/providers/provider-kubernetes.png)     | Kubernetes             | Containers    | ❓    |
|![doc](./assets/providers/provider-docker.png)         | Docker                 | Containers    | ❓    |
|![dos](./assets/providers/provider-dockerswarm.png)    | Docker Swarm           | Containers    | ❓    |
|![ops](./assets/providers/provider-openshift.png)      | Openshift              | Containers    | ❓    |
|![kvt](./assets/providers/provider-kubevirt.png)       | KubeVirt               | Containers    | ❓    |
|![lxd](./assets/providers/provider-lxd.png)            | LXD                    | Containers    | ❓    |


## Backend 

|                                                       | Provider               | Type          | Status | Issue       
|-------------------------------------------------------|------------------------|---------------|--------|-------
|![min](./assets/other/minio.png)                       | MinIO                  | Object Store  | ❓    |
|![inf](./assets/other/influxdb.png)                    | InfluxDB               | Metrics       | ❓    | [#16](https://github.com/mistcommunity/mist-ce/issues/16)
|![vic](./assets/other/victoriametrics.png)             | Victoria Metrics       | Metrics       | ❓    | [#16](https://github.com/mistcommunity/mist-ce/issues/16)
|![mdb](./assets/other/mongodb.png)                     | MongoDB                | DB            | ❓    |
|![hcv](./assets/other/hashicorpvault.png)              | Hashicorp Vault        | Secrets       | ❓    |
|![tfk](./assets/other/traefik.png)                     | Traefik                | Proxy         | ❓    | [#8](https://github.com/mistcommunity/mist-ce/issues/8)
|![ngx](./assets/other/nginx.png)                       | Nginx                  | Proxy         | ❓    |
|![ngx](./assets/other/rabbitmq.png)                    | RabbitMQ               | Message Queue | ❓    | [#18](https://github.com/mistcommunity/mist-ce/issues/18)
|![ngx](./assets/other/elasticsearch.png)               | Elasticsearch          | Logging       | ❓    | [#7](https://github.com/mistcommunity/mist-ce/issues/7)
|![ngx](./assets/other/logstash.png)                    | Logstash               | Logging       | ❓    | 
|![ngx](./assets/other/kibana.png)                      | Kibana                 | Logging       | ❓    | 


# General Overview
> [!NOTE]
> The following is based on the [libcloud docs](https://libcloud.readthedocs.io/en/stable/supported_providers.html)

| Feature                | Status | Issue
|------------------------|--------|----------------------------------------------------------
| Base Compute           | ⚠️    | 
| Block Storage          | ⚠️    | 
| Key Pair Management    | ⚠️    | 
| Load Balancers         | ⚠️    |
| Object Storage         | ⚠️    |
| CDN                    | ⚠️    |
| Object Storage         | ⚠️    |
| Backup                 | ⚠️    |
| DNS                    | ⚠️    |    
| Object Storage         | ⚠️    |
| RBAC                   | ⚠️    | [#3](https://github.com/mistcommunity/mist-ce/issues/3)
| SSO                    | ⚠️    | [#9](https://github.com/mistcommunity/mist-ce/issues/9)
| App Stores             | ✨    | 
| AI MCP API             | ✨    | 
| Plugin System          | ✨    | 



## Base compute
| Provider              | connect | list | create | deploy | reboot | destroy | start | stop | list images | list sizes
|-----------------------|---------|------|--------|--------|--------|---------|-------|------|-------------|-----------
| Amazon Web Services	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Microsoft Azure   	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Google Cloud      	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Alibaba Cloud     	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| IBM Cloud          	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Digital Ocean     	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Equinix Metal     	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Linode             	|✅      |❓    | ❌    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Rackspace         	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Vultr              	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Maxihost            	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Vexxhost         	    |❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| CloudSigma         	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| OpenStack         	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| OnApp              	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| VMWare vSphere        |❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓
| Libvirt              	|❓      |❓    | ❓    |❓	     |❓	    |❓       |❓    |❓    |❓          | ❓


## Block Storage
| Provider              | list | create | destroy | attach | detach | list snapshots | create snapshot
|-----------------------|------|--------|---------|--------|--------|----------------|-----------------
| Amazon EC2        	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓   
| Azure             	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓   
| GCE                	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓   
| Digital Ocean        	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓   
| Equinix Metal        	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓   
| Linode            	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓   
| Rackspace            	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓   
| Vultr                	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓   
| Maxihost             	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓
| CloudSigma           	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓
| OpenStack           	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓
| OnApp                	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓
| VMware vSphere       	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓
| Libvirt              	|❓   | ❓     |❓	     |❓	     |❓      |❓             |❓


## Key pair management
| Provider              | list | get    | create | import string | import file | delete 
|-----------------------|------|--------|--------|---------------|-------------|------------
| Amazon EC2        	|❓   | ❓     |❓	     |❓	           |❓           |❓
| Azure             	|❓   | ❓     |❓	     |❓	           |❓           |❓   
| GCE                	|❓   | ❓     |❓	     |❓	           |❓           |❓ 
| Digital Ocean        	|❓   | ❓     |❓	     |❓	           |❓           |❓  
| Equinix Metal        	|❓   | ❓     |❓	     |❓	           |❓           |❓
| Linode            	|❓   | ❓     |❓	     |❓	           |❓           |❓
| Rackspace            	|❓   | ❓     |❓	     |❓	           |❓           |❓
| Vultr                	|❓   | ❓     |❓	     |❓	           |❓           |❓
| Maxihost             	|❓   | ❓     |❓	     |❓	           |❓           |❓
| CloudSigma           	|❓   | ❓     |❓	     |❓	           |❓           |❓ 
| OpenStack           	|❓   | ❓     |❓	     |❓	           |❓           |❓
| OnApp                	|❓   | ❓     |❓	     |❓	           |❓           |❓
| VMware vSphere       	|❓   | ❓     |❓	     |❓	           |❓           |❓
| Libvirt              	|❓   | ❓     |❓	     |❓	           |❓           |❓


## Load Balancer
| Provider              | create | list | list members | attach member | detach member | attach compute node
|-----------------------|--------|------|--------------|---------------|---------------|-----------------------
| Amazon            	|❓      | ❓  |❓	           |❓	         |❓             |❓
| CloudStack          	|❓      | ❓  |❓	           |❓	         |❓             |❓
| GCE                 	|❓      | ❓  |❓	           |❓	         |❓             |❓
| Rackspace            	|❓      | ❓  |❓	           |❓	         |❓             |❓


## Object Storage (Containers)
| Provider              | list | create | delete 
|-----------------------|------|--------|--------
| Amazon Web Services	|❓   | ❓     |❓	     
| Azure             	|❓   | ❓     |❓	     
| GCE                	|❓   | ❓     |❓
| Digital Ocean        	|❓   | ❓     |❓
| OpenStack           	|❓   | ❓     |❓
| MinIO              	|❓   | ❓     |❓


## Object Storage (Objects)
| Provider              | list | upload | stream upload | download | download part | stream download | streaming partial download | delete
|-----------------------|------|--------|---------------|----------|---------------|-----------------|----------------------------|---------
| Amazon Web Services	|❓   | ❓     |❓	            |❓       |❓             |❓              |❓                          |❓
| Azure             	|❓   | ❓     |❓	            |❓	     |❓             |❓              |❓                          |❓ 
| GCE                	|❓   | ❓     |❓	            |❓	     |❓             |❓              |❓                          |❓
| Digital Ocean        	|❓   | ❓     |❓	            |❓	     |❓             |❓              |❓                          |❓ 
| OpenStack           	|❓   | ❓     |❓	            |❓	     |❓             |❓              |❓                          |❓
| MinIO              	|❓   | ❓     |❓	            |❓	     |❓             |❓              |❓                          |❓


## CDN
| Provider              | enable container | enable object | get container URL | get object URL
|-----------------------|------------------|---------------|-------------------|----------------
| Amazon Web Services	|❓                | ❓           |❓	               |❓       
| Microsoft Azure   	|❓                | ❓           |❓	               |❓       
| Google Cloud      	|❓                | ❓           |❓	               |❓       
| Digital Ocean     	|❓                | ❓           |❓	               |❓       
| OpenStack         	|❓                | ❓           |❓	               |❓       
| MinIO              	|❓                | ❓           |❓	               |❓       


## Containers
| Provider              | install image | list images | deploy | get | start | stop | restart |	destroy | list | list locations
|-----------------------|---------------|-------------|--------|-----|-------|------|---------|---------|------|-----------------
| Docker            	|❓            | ❓          |❓	  |❓   |❓    |❓    |❓      |❓       |❓   |❓       
| Amazon            	|❓            | ❓          |❓	  |❓   |❓    |❓    |❓      |❓       |❓   |❓       
| GCE               	|❓            | ❓          |❓	  |❓   |❓    |❓    |❓      |❓       |❓   |❓       
| Kubernetes           	|❓            | ❓          |❓	  |❓   |❓    |❓    |❓      |❓       |❓   |❓       
| Rancher           	|❓            | ❓          |❓	  |❓   |❓    |❓    |❓      |❓       |❓   |❓       
 

## Containers (Clusters)
| Provider              | create | list | destroy | list 
|-----------------------|--------|------|---------|------
| Docker            	|❓     | ❓   |❓      |❓   
| Amazon            	|❓     | ❓   |❓      |❓   
| GCE               	|❓     | ❓   |❓      |❓   
| Kubernetes            |❓     | ❓   |❓      |❓   
| Rancher           	|❓     | ❓   |❓      |❓   


## Backup (Targets)
| Provider              | get types | list | create | create from node | create from storage container | update | delete | recover  
|-----------------------|-----------|------|--------|------------------|-------------------------------|--------|--------|-----------
| Amazon            	|❓        | ❓   |❓     |❓                |❓                            |❓      |❓     |❓
| GCE                   |❓        | ❓   |❓     |❓                |❓                            |❓      |❓     |❓


## Backup (Jobs)
| Provider              | list points | recover | list | create | resume | suspend | cancel 
|-----------------------|-------------|---------|------|--------|--------|---------|-----------
| Amazon            	|❓           | ❓     |❓    |❓     |❓     |❓       |❓    
| GCE               	|❓           | ❓     |❓    |❓     |❓     |❓       |❓    


## DNS
| Provider              | list zones | list records | create zone | update zone | create record | update record | delete zone | delete record
|-----------------------|------------|--------------|-------------|-------------|---------------|---------------|-------------|---------------
| Cloudflare           	|❓          | ❓          |❓          |❓           |❓            |❓             |❓          |❓
| Digital Ocean        	|❓          | ❓          |❓          |❓           |❓            |❓             |❓          |❓
| Google            	|❓          | ❓          |❓          |❓           |❓            |❓             |❓          |❓
| Linode            	|❓          | ❓          |❓          |❓           |❓            |❓             |❓          |❓
| OnApp             	|❓          | ❓          |❓          |❓           |❓            |❓             |❓          |❓
| Rackspace           	|❓          | ❓          |❓          |❓           |❓            |❓             |❓          |❓
| Voltr             	|❓          | ❓          |❓          |❓           |❓            |❓             |❓          |❓