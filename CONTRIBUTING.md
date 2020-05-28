# You can help contribute to the atc-data

The atc-data project is in a constant state of development. We are always on the lookout for new information to help refine and extend what is covered. If you have additional data requirements or have other relevant information, then we would like to hear from you.

All contributions and feedback to the atc-data are appreciated. Please don't hesitate to tell us what do you think could be improved by [submitting GitHub issue](#how-to-submit-an-issue).

# How to add a new Data Needed, Logging Policy or Enrichment?

If you would like to contribute one of the listed entities, you need to follow [How to add a new feature or create a pull request](#how-to-add-a-new-feature-or-create-a-pull-request) guidelines, points 1, 2, 3, 5, 7, 8, bypassing 4 and 6, as you don't need the development environment.

Please use special templates for the entities to develop new ones:

- [Data Needed template](data_needed/dataneeded.yml.template)  
- [Logging Policy template](response_actions/respose_action.yml.template)  
- [Enrichment template](logging_policies/loggingpolicy.yml.template)  

# How to submit an issue?

First, please refer to [contribution-guide.org](http://www.contribution-guide.org/) for the steps we expect from contributors before submitting an issue or bug report. Be as concrete as possible, include relevant logs, package versions etc.

The proper place for open-ended questions is [Slack](https://join.slack.com/t/atomicthreatcoverage/shared_invite/zt-6ropl01z-wIdiq3M0AEZPj_HiKfbiBg) or [Telegram](https://t.me/atomic_threat_coverage). 

# How to add a new feature or create a pull request?

1. Fork the [atc-data repository](https://github.com/atc-project/atc-data)
2. Clone your fork: `git clone https://github.com/<YOUR GITHUB USERNAME>/atc-data.git`
3. Create a new branch based on `develop`: `git checkout -b my-feature develop`
4. Setup your Python enviroment
   - Create a new [virtual environment](https://virtualenv.pypa.io/en/stable/): `pip install virtualenv; virtualenv atc_env` and activate it:
      - For linux: `source atc_env/bin/activate` 
      - For windows: `atc_env\Scripts\activate`
   - Install ATC and its test dependencies in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs) — `pip install -r requirements.txt`
5. Implement your changes
6. Check your code for PEP8 requirements
7. Add files, commit and push: `git add ... ; git commit -m "my commit message"; git push origin my-feature`
8. [Create a PR](https://help.github.com/articles/creating-a-pull-request/) on Github. Write a **clear description** for your PR, including all the context and relevant information, such as:
   - The issue that you fixed, e.g. `Fixes #123`
   - Motivation: why did you create this PR? What functionality did you set out to improve? What was the problem + an overview of how you fixed it? Whom does it affect and how should people use it?
   - Any other useful information: links to other related Github or mailing list issues and discussions, benchmark graphs, academic papers…
   - Note that your Pull Request should be into the **develop** branch, **not master**
