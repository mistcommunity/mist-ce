+++
title = "Setting Up Mist"
weight = 2
+++

Setting up management and monitoring of your infrastructure is a matter of a few, simple steps. Let's go through them:

### Step 1: Registration
{{< tip "warning" >}}
Registration  is not relevant for mist-ce
{{< /tip >}}
Head over to  https://mist.io and register for an account. Once you complete the form, you’ll get a confirmation e-mail. Click on the confirmation link and you’ll be transferred back and logged in to Mist.io. Alternatively, you can sign up with your Google or Github account.

<p align="center">
  <img src="/images/registration.png">
</p>

### Step 2: Adding your servers
If you’re adding cloud-based servers, you’ll need your API keys or your username and password, depending on the provider. If you want to add a bare-metal server, you’ll need the server’s IP and your username. If you are not sure where to find them, we’ve put together instructions for each provider to help you. To add your servers, click on the **Add cloud button**, choose your provider (or *other server*) and fill in the details.

<p align="center">
  <img src="/images/add-cloud.png">
</p>

### Step 3: Making your servers connectable by Mist.io
Mist.io works better if you connect it to your servers using SSH in order to help you with setting up monitoring and enable the web shell. If SSH access is not possible or desirable, you can choose to manually install the collectd monitoring agent (as explained in the next section) but you'll be missing some features. To connect your server, first head over to the keys section and click on the Add button to set up your keypairs. 

<p align="center">
  <img src="/images/add-key.png">
</p>

If you already have a private SSH key that you use to connect to the server, you can import it in Mist.io by pasting your private key on the text dialog or by uploading the key file. 

If you want to create a new keypair, click on the Generate button to create a new SSH key and then on Add to add it to Mist.io. On the Keys section click on the key you created and copy the Public Key. Paste the public key on your server's ~/.ssh/authorized_keys file. For example, if you want to deploy this key on a server for the root user, you will need to paste the public key on file /root/.ssh/authorized_keys. If the /root/.ssh folder does not exist, you have to create it and set the correct permissions. Then paste the public key

```shell
mkdir /root/.ssh 
chmod -R 700 /root/.ssh 
cat > /root/.ssh/authorized_keys 
...
```

Once you have a key pair set up, it is time to associate it with your server. Head over to Machines section and then on your server's page. On the top right, click on keys, and then on Add key and select your newly added key. Mist.io will try to connect to the server on port 22 as the root user. If it succeeds your key will be added on the list. If it fails it will prompt you to provide an alternative username and port. 

From now on, Mist.io can deploy your key automatically on any new servers created through the service. You can find more information regarding key management  here.

### Step 4: Enabling monitoring
**a) If you've set up SSH access**

If your server is connectable by Mist.io, you’ll see a blue bar appearing next to it on your machine list, indicating your server’s load. Click on the machine to go to the detailed view and then on the Enable button in the Monitoring section. Mist.io will then install the collectd open source agent and you'll start seeing the monitoring graphs once it is done.

<p align="center">
  <img src="/images/monitoring.jpg">
</p>

**b) Manual installation**

If you don't want to give SSH access to Mist.io, you can always install the monitoring agent manually. Click on Enable Monitoring on your server and Mist.io will open a popup with a command that you can run on your server to install the agent.

<p align="center">
  <img src="/images/monitoring-agent.jpg">
</p>

If you are wondering what the command does, it downloads and runs a python script with two arguments, a uuid and a password. This will be provided to collectd in order to encrypt the packages containing monitoring data, so that mist.io knows what server it talks to. The script (https://github.com/mistio/deploy_collectd/raw/master/local_run.py) will create a python virtual environment that will install ansible open source configuration management library inside the virtual environment and then run an ansible playbook (https://github.com/mistio/deploy_collectd/) that will install on the system collectd open source agent, and set it's configuration on /opt/mistio-collectd. Only dependency for the monitoring to function is that Python 2 is available on the system.

Step 5: Setting up alerting
Once monitoring is enabled, a graph will appear. Click on the Add Rule button just below the graph to set up your first alerting rule. E.g. if you want to get an email once the load exceeds 4, your rule should look like this:

<p align="center">
  <img src="/images/alert-rule-1.jpg">
</p>

Assuming you have a process that’s leaking memory, you can set up Mist.io to restart that process once your memory usage exceeds 95%.

<p align="center">
  <img src="/images/alert-rule-2.jpg">
</p>

Thats it. You’ve successfully set up monitoring for your server and added your first alerting rules.