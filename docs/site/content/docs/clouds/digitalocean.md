---
title: "Digital Ocean"
weight: 6
---

Mist.io supports the current  DigitalOcean's API (version 2). In order to connect a Digital Ocean cloud to mist.io, you'll need a valid Token. To obtain one, log in to your Digital Ocean account, click on the 'Apps & API' link on the left side menu and then Generate new token. Specify a Token Name and if it is going to be Read or Write. If you're going to create Droplets, this has to be Write.

Press Generate Token, and copy the Token created. The token appears once, if you forget it there's no way to retrieve it, but can easily create a new one. 

<p align="center">
  <img src="/images/clouds/do-token.png">
</p>

Generate a token by pressing 'Generate new token'

Back on Mist.io, press 'Add cloud' and select DigitalOcean from the drop list. Enter the token you have generated before and press Add.

<p align="center">
  <img src="/images/clouds/do-add.png">
</p>

You should now see your Droplets in the Machines section. 

<p align="center">
  <img src="/images/clouds/do-droplets.png">
</p>

You can now run actions (reboot, stop, destroy), create and provision new Droplets, provide an ssh key and connect through a web console, and enable monitoring to be able to see performance diagrams and set alerts.