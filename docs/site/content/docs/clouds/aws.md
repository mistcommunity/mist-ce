---
title: "AWS"
weight: 1
---

To add an Amazon EC2 cloud you will need to add an AWS Identity and Access Management (IAM) user and provider the key/secret combination. In order to achieve this task login to your Amazon console. On the top right select your user name and choose 'Security Credentials' from the drop down menu.

<p align="center">
  <img src="/images/clouds/aws-credentials.png">
</p>

A popup will ask you to use IAM users, click on ' Get started with IAM Users', this will get you to the user listing page

<p align="center">
  <img src="/images/clouds/aws-iam-users.png">
</p>


Click on 'Create new users' on the top left, specify a username and make sure option 'Generate an access key for each user' is enabled. Then press create. 

<p align="center">
  <img src="/images/clouds/aws-generate-access-key.png">
</p>

User has been created and you are notified that the credentials are created as well, select ' Show User security credentials' and make sure you write down the creds on a file.

<p align="center">
  <img src="/images/clouds/aws-show-credentials.png">
</p>


Before you can use these credentials however you will need to attach a Policy to the user. Close the window and you will be directed to the list of the users. Select the user you have just created and enter Attach Policy on the Permissions tab. From the list of policies select AmazonEC2FullAccess  and save. 

<p align="center">
  <img src="/images/clouds/aws-permissions.png">
</p>


You are now ready to provide to mist.io the credentials you have just created. Specify the Access Key ID as key and the Secret Access key as secret . Select your EC2 region and press Add

<p align="center">
  <img src="/images/clouds/aws-add-mist.png">
</p>

The cloud will be added and you will be able to see a listing of your current VMs, run actions and deploy new ones. 

