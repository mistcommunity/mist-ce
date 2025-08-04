---
title: "Azure"
weight: 2
---

Mist helps you manage your Microsoft Azure infrastructure across regions and alongside other supported clouds.

Specifically for Microsoft Azure, with Mist you can:

- View a list of your VMs. Listings include all metadata information, e.g. IP, price, status etc.
- Start, stop, reboot and delete VMs.
- Create new VMs.
- View, create and destroy volumes.
- Attach volumes to VMs and detach them.
- View networks.

You can also leverage features that are common to all our supported clouds, e.g. tags, ownership metadata, expiration dates, cost quotas, role-based access controls, shell, scripts, orchestration, monitoring, rules, audit logs etc.

## Getting started

<p align="center">
  <img src="/images/clouds/azure-getting-started.png">
</p>

You can connect Microsoft Azure to Mist in four simple steps:

1. Get your Azure REST API credentials. This is easier from the command line either with az CLI or Azure's Cloud Shell. Follow the instructions at https://docs.microsoft.com/en-us/rest/api/azure/. To go directly to the relevant part of the video, check out https://youtu.be/6b1J03fDnOg?t=139. The part that interests you starts at 2:19 and runs until 4:33.
2. Log in Mist, go to the add cloud form at https://mist.io/clouds/+add and click the Microsoft Azure logo.
3. Fill in the form with the credentials you got from step one above. Please remember that Mist's "Tenant ID" is Azure's "tenant", Mist's "Client key" is Azure's "appId" and Mist's "Client secret" is Azure's "password". The "Subscription ID" is the same in both.
4. Click the "ADD CLOUD" button.

In a few seconds, Mist will auto-discover the resources in your account and will show you a cost estimate for them.