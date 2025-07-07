---
title: "Observation Logs"
weight: 2
---

Mist emits observation logs whenever it detects changes in your infrastructure. This way, you can even keep track of actions that did not happen through Mist’s API.

In more detail, Mist emits observation logs when it detects:

creation or destruction of machines, volumes, networks and DNS zones,
changes in the size of machines (e.g. a machine was resized from 2 vCPUs to 4),
changes in the status of machines (e.g. a machine went from running to stopped),
block storage volumes getting attached or detached
Observation logs are shown in the logs widget and their type is always set to observation. To search specifically for observations logs, you should include **type:observation** in your query. For more complicated queries, keep in mind that Mist leverages Elastic's string query syntax.



The USER column is empty because these actions did not happen through Mist’s API. You can click on each log entry to get more information on what happened and which resources were involved.

Please keep in mind that observation logs are supported in Mist v4.2 and later. They are available in all Mist editions, including Mist Community Edition (CE).

<p align="center">
  <img src="/images/observation.png">
</p>