---
title: "VMware vSphere"
weight: 5
---

Mist helps you manage your infrastructure on VMware vSphere alongside other supported clouds. This helps you manage hybrid and multi-cloud setups from a single pane of glass.

Mist supports vSphere versions v4.0 to v7.0 through their SOAP API. With Mist you can:

- View your VMs and their metadata, e.g. IP, image, state etc.
- Start, stop, reboot and delete VMs.
- Take snapshots of VMs.
- Create new VMs. Provisioning requires the existence of templates, OVF files or a content library.
- Connect to your VMs using a VNC console through the web. For the console to work, the relevant host must be reachable by Mist.

You can also leverage features that are common to all our supported clouds, e.g. tags, ownership, expiration dates, cost quotas, RBAC, shell, scripts, orchestration, monitoring, rules, audit logs etc.

## Getting started

<p align="center">
  <img src="/images/clouds/vmware-getting-started.png">
</p>

To get started with vSphere in Mist you first need to add a vSphere cloud. In more detail:

1. Log in Mist.
2. Go to Mist's add cloud form at https://mist.io/clouds/+add and click the vSphere logo.
3. Type a name for your cloud in the "Title" field.
4. Type the hostname or IP of your vCenter cluster.
5. Type your vCenter username and password. Please keep in mind that Mist will only be able to perform whatever actions are allowed to this user.
6. It is recommended to provide a CA certificate. To get the certificate, go to vCenter's login page and click on "Download trusted root CA certificates". Extract the zip file you downloaded and open the lin/*.0 file. Copy the contents and paste them to the "CA Certificate" field.   
7.Click the "ADD CLOUD" button and you are ready to go.