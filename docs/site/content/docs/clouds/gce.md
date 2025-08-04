---
title: "GCE"
weight: 3
---

Mist helps you manage your Google Cloud projects across any region and alongside other supported clouds.

Specifically for Google Cloud, with Mist you can:

- View a list of your VMs. Listings include all metadata information, e.g. IP, price, status etc.
- Start, stop, reboot and delete VMs.
- Create new VMs.
- View, create and destroy volumes.
- Attach volumes to VMs and detach them.
- View, create and destroy networks.
- View, create and delete Cloud DNS zones and records.

You can also leverage features that are common to all our supported clouds, e.g. tags, ownership metadata, expiration dates, cost quotas, role-based access controls, shell, scripts, orchestration, monitoring, rules, audit logs etc.

## Getting started

<p align="center">
  <img src="/images/clouds/gce-getting-started.png">
</p>

You can connect Google Cloud to Mist in five simple steps:

1. In Google Cloud, create a new service account key as shown here https://cloud.google.com/iam/docs/creating-managing-service-account-keys. Note your project ID and download your private key file, which is in JSON format.
2. Log in Mist, go to the add cloud form at https://mist.io/clouds/+add and click the Google Cloud logo.
3. Fill in your project ID and the contents of the key file in the respective fields.
4. If you wish to also manage your DNS records in Google Cloud DNS through Mist, toggle the "Enable DNS support" switch. By default this is set to off.
5. Click the "ADD CLOUD" button.

In a few seconds, Mist will auto-discover the resources in your account and will show you a cost estimate for them.