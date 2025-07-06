# 💡 Contributing

Thank you for contributing to Mist Community Edition! 🎉

This project is undergoing active restoration and modernization. We are identifying what works, what’s broken, what’s necessary, and what can be removed. 🤔

The roadmap and features will continually evolve based on pull requests and discussions. 🗪

Whether you're new to open source or a seasoned contributor, there's something you can help with! 🤗

## 🔗 Quick Links

|  | Link                                                            | Description
|--|-----------------------------------------------------------------|-----------------
|⚠️|[ISSUES](https://github.com/mistcommunity/mist-ce/issues)        | Check for bug reports & feature requests
|🔀|[PULL REQUESTS](https://github.com/mistcommunity/mist-ce/pulls)  | Existing pull requests
|👨🏻‍💻|[DEVELOPERS](./DEVELOPERS.md)                                    | Guide on developing
|📝|[CHANGELOG](./CHANGELOG.md)                                      | Current and legacy changelog
|✨|[FEATURES](./FEATURES.md)                                        | Feature tracking list
|🗺️|[ROADMAP](./ROADMAP.md)                                          | Rough development roadmap
|🌿|[BRANCHES](./BRANCHES.md)                                        | Audit of legacy branches
 
## 🏃‍♀️‍➡️ Getting Started

- [ ] Check [issues](https://github.com/mistcommunity/mist-ce/issues) and [discussions](https://github.com/mistcommunity/mist-ce/discussions) for existing bugs or feature requests.
- [ ] Skim through the [FEATURES.md](./FEATURES.md) and [ROADMAP.md](./ROADMAP.md) to understand the project’s direction.
- [ ] Review [DEVELOPERS.md](./DEVELOPERS.md) to set up your development environment.
- [ ] If you encounter a new bug or idea, open a new issue with as much detail as possible.

### Ways to contribute
|  | Area       | Description
|--|------------|------------
|📄| Docs       | We use [Hugo](https://gohugo.io/) for documentation under `/docs/site`. Help keep it up to date!
|🧪| Testing    | Manual and automated testing are both welcome, especially as we re-enable CI workflows.
|🌿| Branches   | Help us audit and clean up the 190+ legacy branches.
|📱| UI         | The UI is built with deprecated Polymer components. We're migrating to [Lit](https://lit.dev), and possibly a modern framework later.
|⚙️| API        | The backend uses Python Pyramid and Apache Libcloud. We're reviewing future options due to Libcloud’s maintenance status.
|🤖| Automation | Automate anything! Examples include container workflows, CI/CD, or AI agent instructions (e.g. `AGENTS.md` or `Cursor rules`).
|🔒| Security   | Test the security of mist-ce on a self-hosted instance.

## 🌿 Versioning and Branching
> [!IMPORTANT]
> Subject to change. We follow historical semantic versioning where possible, with plans to simplify. See [BRANCHES.md](./BRANCHES.md) for more on the current cleanup effort.

> The latest minor version will be the default branch. 

1. The latest minor version (e.g., `4.8.x`) has:
   - A **stable** branch (`4.8.x`)
   - A **staging** branch (`4.8.x-staging`) for incoming PRs
2. Pull requests should target the `-staging` branch.
3. After review and testing, changes are merged into the stable branch.
4. Version tags are created on release (e.g., `v4.8.1`).
5. GitHub Actions build and push Docker images tagged with the version and `latest`.

Only one branch for each major version will be kept.




## 🤗 Code of Conduct

Please read our [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) to help maintain a respectful and inclusive environment.