---
title: "Linode"
weight: 7
---

Mist helps you manage Linode alongside other supported clouds. 

Specifically for Linode, with Mist you can:

- View your VMs and their metadata, e.g. IP, image, price etc.
- Start, stop, reboot, resize and delete VMs.
- Create new VMs.
- View, create, attach, detach and delete volumes. 
- Create & manage your DNS zones
- You can also leverage features that are common to all our supported clouds, e.g. tags, ownership metadata, expiration dates, cost quotas, role-based access controls, shell, scripts, orchestration, monitoring, rules, audit logs etc.

## Getting started

<p align="center">
  <img src="/images/clouds/linode-getting-started.png">
</p>

You can connect Linode to Mist in five simple steps:

1. Go to Linode's API token section at https://cloud.linode.com/profile/tokens and create a new API token for Mist. Please keep in mind that the scope of this token will limit what actions you can perform through Mist. We recommend setting Domains, Images, IPs, Linodes and Volumes to Read/Write and the rest to Read Only. When/if your token expires, you will need to create and new one and update the relevant cloud in Mist.
2. Log in Mist, go to the add cloud form at https://mist.io/clouds/+add and click the Linode logo.
3. Paste your Linode API token in the relevant field.
4. If you wish to also manage your DNS records in Linode through Mist, toggle the "Enable DNS support" switch. By default this is set to off.
5. Click the "ADD CLOUD" button.
In a few seconds, Mist will auto-discover the resources in your account and will show you a cost estimate for them.