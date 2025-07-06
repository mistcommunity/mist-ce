# 🌿 Branches

The `mist-ce` repository contains 190+ legacy branches from over 8 years of development. Many are unmerged, untagged, and their purpose is unclear. Some use a now-abandoned submodule structure; others are partial experiments or future version stubs.

> [!IMPORTANT]
> The following is just a proposal, see the [Discussion](https://github.com/mistcommunity/mist-ce/discussions/28).

<br>
<hr>

## 🧱 Current Challenges
🚧 No clear mapping between branches and versions \
❌ No guarantee any branch actually works or builds \
❓ Unknown whether fixes/features exist in abandoned branches \
🔁 Some future-version branches exist but can't be tested
💥 Likely merge conflicts due to huge divergence \
🧹 We can't keep everything, but we also don't want to lose anything important 


> [!NOTE]
> We're developing a process to review, log, and collapse historical work into structured version branches going forward.

See [ROADMAP](./ROADMAP.md) and [CHANGELOG](./CHANGELOG.md)


<br>
<hr>

## ✅ Branching Strategy
We now follow a minor version branching convention based on semantic versioning, for example:

```
v4.8              ← stable minor release branch (latest - default branch)
v4.8-staging      ← testing branch for PRs before release
v3                ← historical major release
v2                ← historical major release
v1                ← historical major release
```

### Proposed Guide:

1. Contributors fork the repo
2. Create a new branch for the feature / fix (prefix with the version, e.g. v4.8.x-docs)
3. PRs target the *-staging branch.
4. After testing and review, changes are merged to the matching minor stable branch.
5. We tag patch releases as v4.8.1, v4.8.2, etc.
6. Docker images are built/tagged automatically by GitHub Actions.

```
v4.8.x                    ← stable (release) branch
 └── v4.8.x-staging       ← PRs merged here first for testing
      └── v4.8.x-docs-fix ← your feature branch
```

<br>
<hr>

## 🗃️ Historical Branch Audit Plan
We are performing a one-time audit to review and retire all legacy branches. The current suggested approach is:

🔍 Step-by-Step
> This is easiest in the GitHub UI, but can be done with Git CLI

1. Gander at the [branch list](https://github.com/mistcommunity/mist-ce/branches/all)
2. The "updated" age has been modified, the original branch list is here [mistio/mist-ce](https://github.com/mistio/mist-ce/branches/all)
3. Compare each branch to master, which can be done in the GitHub UI
4. Classify as per the legend below
5. Record notes to what the changes are
6. Merge in to v4.8.x-staging ← ***Unclear if this is the best approach***
7. Test if possible, otherwise merge to v4.8.x
8. Increment and tag the patch version (v4.8.69420)


<br>
<hr>

## 🧩 Suggested Policy
For future clarity, all non-version branches must include:
 > - The version they relate to (e.g., 4.8.x-fix-auth)
 > - A short, descriptive slug
 > - Must target the *-staging branch in PRs


<br>
<hr>

## 🗓️ Long-Term Goal
Reduce the branch list to:
> - One branch for the latest active major.minor version
> - One -staging branch for the latest major.minor version
> - One branch per historical major version (v3, v2)
> - Maybe a legacy reference branch (legacy/old-submodules) with historical commits


## 🧾 Audit

```
✅ Keep        → still relevant or tied to supported version
🔥 Delete      → no value, stale, or merged already
🔀 Merge       → then delete: contains fixes/features to rebase into 4.8.x-staging
❓ Check       → needs further investigation
```

<br>

|   | Branch                            | Type      | Status | Notes                      
|---|-----------------------------------|-----------|--------|----------------------------------------------------
|✅| v4.8.x                            | version   | keep   | v4.8.x - Latest - current default             
|✅| v4.8.x-staging                    | version   | keep   | v4.8.x - Testing and staging          
|✅| v4.7.x                            | legacy    | keep   | v4.7.x - Stable, keep for reference (state before mistcommunity fork)
|🔥| master-backup                     | legacy    | temp   | Reference prior to mono-repo (maybe keep as v4.7.x??)
|🔥| monorepo                          | legacy    | delete | Branch when creating monorepo
|✅| master                            | default   | keep   | Latest  stable (monorepo)
|🔀| feat/scaleway                     | feature   | merge  | To merge in to v4.8.x
|🔀| v4.7.x-dev                        | develop   | merge  | Prior to using forks, to merge in to v4.8.x
|🔀| v4.7.x-dev-elasticsearch-draft    | develop   | merge  | Prior to using forks, to merge in to v4.8.x
|🔀| v4.8.x-docs                       | develop   | merge  | Temp branch to update docs while detaching fork from upstream, merge in to v4.8.x
|❓| wtf3                              | legacy    | check  | 
|❓| wtf3                              | legacy    | check  | 
|❓| workers                           | legacy    | check  |
|❓| w8-navigation-menu                | legacy    | check  |
|❓| vsphere-test                      | legacy    | check  |
|❓| vsRest                            | legacy    | check  |
|❓| vpa-recommendations               | legacy    | check  |
|❓| volume-ownership                  | legacy    | check  |
|❓| vnfs                              | legacy    | check  |
|❓| vexxhost-openstack                | legacy    | check  |
|❓| vault-integration-api-v2          | legacy    | check  |
|❓| vault-integration                 | legacy    | check  |
|❓| v5                                | legacy    | check  |
|❓| v5-tests                          | legacy    | check  |
|❓| v4.4.x                            | legacy    | check  |
|❓| v2-tests                          | legacy    | check  |
|❓| user-create                       | legacy    | check  |
|❓| upstream-tags                     | legacy    | check  |
|❓| update-selenium                   | legacy    | check  |
|❓| update-requirements               | legacy    | check  |
|❓| update-paramiko                   | legacy    | check  |
|❓| update-libcloud                   | legacy    | check  |
|❓| update-helm                       | legacy    | check  |
|❓| update-gitlab                     | legacy    | check  |
|❓| update-dind                       | legacy    | check  |
|❓| update_as_dict                    | legacy    | check  |
|❓| ui-test-requests                  | legacy    | check  |
|❓| tweak-resource-req-and-limits     | legacy    | check  |
|❓| timescaledb_support               | legacy    | check  |
|❓| test-mistio-trunk                 | legacy    | check  |
|❓| test-enhance-selectors            | legacy    | check  |
|❓| test-cloud-images                 | legacy    | check  |

...and many, many more to add here.