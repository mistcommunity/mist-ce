+++
title = "Managing Infrastructure"
weight = 3
+++

Now that you've set up Mist.io to monitor your infrastructure, lets delve a bit on the Mist.io UI and what you can do with it.

Once you've added a couple of clouds and enabled monitoring for some of your VMs, Mist.io's homepage should look similar to this one:

<p align="center">
  <img src="/images/homepage.jpg">
</p>

At the top, there is the list with the connected clouds. A yellow dot indicates that Mist.io could not connect to that cloud for a while, and has disabled it.

On the left, you can see the main sections of your infrastructure: Machines (your VMs), Images (private, public cloud images or Docker), Networks, Keys (your SSH keys stored in Mist.io) and Scripts. Next to it there is a list with the most important latest incidents. Below, there is a graph that displays a quick view of the load for each of your servers that has monitoring enabled. At the bottom, you can find a detailed activity log. 

### Machines
The Machines section is where most of the magic happens. After clicking on the Machines button, you should see a list of all your servers, neatly tagged with their provider for easier access:

<p align="center">
  <img src="/images/machines.png">
</p>

Machine Details

Clicking on one of the buttons will take you to a detailed list for that VM. If monitoring is enabled, you should see something similar to this:

<p align="center">
  <img src="/images/machine-details.jpg">
</p>

At the top, you can see the monitoring graphs for various server or application metrics. You can add more by clicking on the Add Graph button. Mist.io has several pre-built graphs, and you can add your own by installing collectd plugins or by writing your own. Right under the graphs, there is a list of rules. Rules, are thresholds that you set and you can specify actions to be taken once that threshold has been exceeded.

Below the rules, there is a detailed overview of your server: When it was last probed by Mist.io, its' uptime, the current load, etc.

### Tags, actions and the web console
At the bottom you can see three buttons: Tags, Shell and Actions. The first one allows you to manage that machine's tags. Tags can help you group machines and make them easier to find and orchestrate.

If you have an SSH key installed and Mist.io has succesfully established an SSH connection to that server, the Shell button will also be active. Clicking on the Shell button will open a fully featured web console.

<p align="center">
  <img src="/images/web-console.png">
</p>

Finally, there is the Actions button, marked with three dots (...). Clicking on the button will open a menu with actions that you can perform on that server. Each cloud provider allows its' own set of actions depending on the state of the virtual machine, but most of them allow the most typical: shutdown, reboot and destroy.

<p align="center">
  <img src="/images/machine-actions.png">
</p>

### Images

Images, are premade virtual machine or container blueprints that can be used to bootstrap your newly created instances. Mist.io supports images from public and private clouds and Docker engines. For example, this is a sample list from Google Compute Engine:

<p align="center">
  <img src="/images/images.png">
</p>

You can search among thousands of images and launch new VMs by clicking on one of them. For instance, clicking on the last one will open the Create Machine wizard with the image pre-selected:

<p align="center">
  <img src="/images/create-machine.jpg">
</p>

With Mist.io, you get a central place to find and use Docker and cloud images. When using Docker, Mist.io will give you a listing that includes the default Mist.io images, along with the images that are available on your Docker engine.

### Networks
Cloud Networks are software-defined networks that offer complete control over your network topology, IP addressing (IPv4 or IPv6), and architecture. Mist.io supports cloud networks for most public and private clouds. Clicking on the Networks button will show you a list of all your networks tagged by provider:

<p align="center">
  <img src="/images/networks.png">
</p>

You can optionally create a subnet and specify the network address.

### Keys
The Keys section is where you can manage your SSH keys. 

<p align="center">
  <img src="/images/keys.png">
</p>

You can generate new keys or import existing ones to Mist.io. To create a new keypair, navigate to the Keys section and click the Add key button:

You can choose to generate a new 2048 bit RSA key, or import your own by uploading a key file or by pasting your private key on the text box.

<p align="center">
  <img src="/images/add-key.png">
</p>

Click on Create and your key will be associated with your Mist.io account (or stored locally if you're using the open source version). The machines that will be created afterwards through mist.io will have your key automatically deployed. To use your key with an existing server, navigate to the Keys section, click on your key, copy the Public Key

<p align="center">
  <img src="/images/public-key.png">
</p>

and paste it inside your machine's "~/.ssh/authorized_keys' file.

### Scripts
Last but not least, is the Scripts section. Here, you can create and store scripts to automate repetitive actions. You can run these scripts on your existing virtual machines or on newly created ones. Mist.io currently supports Ansible and executable scripts. There are three ways to add your script to Mist.io. Through github, through a URL or by pasting it directly on the add script wizard

<p align="center">
  <img src="/images/scripts.png">
</p>