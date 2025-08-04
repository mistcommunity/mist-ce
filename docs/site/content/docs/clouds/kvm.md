---
title: "KVM"
weight: 4
---

Mist helps you manage infrastructure on any number of KVM hosts and guests (VMs) alongside other supported clouds.

Specifically for KVM, with Mist you can:

- View your hosts, guests and their metadata, e.g. image, state etc.
- Start, stop, suspend, clone, reboot and delete VMs.
- Create new VMs.
- If you use virtual network functions (VNFs) over SR-IOV, you can chose which ones you'd like to use during VM creation.
- Connect to your VMs using VNC console through the web.

You can also leverage features that are common to all our supported clouds, e.g. tags, ownership, expiration dates, cost quotas, RBAC, shell, scripts, orchestration, monitoring, rules, audit logs etc.

## Getting started

<p align="center">
  <img src="/images/clouds/kvm-getting-started.png">
</p>

To get started with KVM in Mist you first need to add a KVM cloud. In more detail:

1. Log in Mist.
2. Go to Mist's add cloud form at https://mist.io/clouds/+add and click the KVM logo.
3. Type a name for your cloud in the "Title" field.
4. Type the hostname or IP of the host and optionally an alias.
5. Select an existing SSH key or upload one. This key will be used to communicate with the host. Please keep in mind that Mist doesn't support passphrase-protected keys.
6. Input the SSH username and port to connect to. The SSH user in this field should have the right to execute virsh commands.
7. Type the path where Mist will look for images.
8. If you have more hosts to add to this cloud, click the "+" icon and repeat steps (4) - (7) above.
9. Click the "ADD CLOUD" button and you are ready to go.