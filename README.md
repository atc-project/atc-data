# atc-data

![](docs/images/logo_v2.png)

The atc-data is a community-driven project designed to accumulate and describe specific data that is required by Security Operations, such as Threat Detection/Hunting and Incident Response.  

It includes a description of event logs, network telemetry, data lists, and so on. And with that — a detailed description of what has to be configured and how the data has to be processed to be used in the Security Operations.  

The main advantage of the project is a clear, exact definition of where specific data is required, whether it's a Detection Rule, Response Action, or Visualisation.  

The main use cases:

- Data collection prioritization. And with that — Threat Detection/Hunting and Incident Response capabilities development
- Gap analysis — determine "coverage" of existing Threat Detection/Hunting and Incident Response capabilities, depending on data collected

The main resources:

- Automatically generated atc-data [website](https://atc-project.github.io/atc-react/) is the best place for getting details about existing analytics  
- Automatically generated [Atlassian Confluence knowledge base](https://atomicthreatcoverage.atlassian.net/wiki/spaces/REACT/pages/755469668/Response+Stages) - exporting functionality demonstration  

## Actionable Analytics

The ATC RE&CT project inherits the "Actionable Analytics" paradigm from the [ATC](https://github.com/atc-project/atomic-threat-coverage) project, which means that the analytics are:

- **human-readable** (`.md`) for sharing/using in operations
- **machine-readable** (`.yml`) for automatic processing/integrations
- **executable** by Incident Response Platform ([TheHive Case Templates](docs/thehive_templates/) only, at the moment)

Simply saying, the analytics are stored in `.yml` files, that are automatically converted to `.md` documents (with [jinja](https://palletsprojects.com/p/jinja/)) and `.json` TheHive Case Templates.  

### Data Needed

to be collected to produce detection of specific Threat

This entity expected to simplify communication with SIEM/LM/Data Engineering teams. It includes the next data:

- Sample of the raw log to describe what data they could expect to receive/collect
- Description of data to collect (Platform/Type/Channel/etc) — needed for calculation of mappings to Detection Rules and general description
- List of fields also needed for calculation of mappings to Detection Rules and Response Playbooks, as well as for `pivoting.csv` generation

Response Action is a description of a specific atomic procedure/task that has to be executed during the Incident Response. It is an initial entity that is used to construct Response Playbooks.  

Here is an example of Response Action:

<details>
  <summary>Initial YAML file (click to expand)</summary>
  <img src="docs/images/ra_yaml_v5.png" />
</details>

- Automatically created [Markdown file](docs/Response_Actions/RA_2202_collect_email_message.md)
- Automatically created [mkdocs web page](https://atc-project.github.io/atc-react/Response_Actions/RA_2202_collect_email_message/)
- Automatically created [Confluence page](https://atomicthreatcoverage.atlassian.net/wiki/spaces/REACT/pages/755435640/RA2202+Collect+email+message)

The categorization aims to improve Incident Response process maturity assessment and roadmap development.  

### Logging Policies

need to be configured on data source to be able to collect Data Needed

This entity expected to explain SIEM/LM/Data Engineering teams and IT departments which logging policies have to be configured to have proper Data Needed for Detection and Response to specific Threat. It also explains how exactly this policy can be configured.

### Enrichments

for specific Data Needed which required for some Detection Rules

This entity expected to simplify communication with SIEM/LM/Data Engineering teams. It includes the next data:

- List of Data Needed which could be enriched
- Description of the goal of the specific Enrichment (new fields, translation, renaming etc)
- Example of implementation (for example, Logstash config)

This way you will be able to simply explain why you need specific enrichments (mapping to Detection Rules) and specific systems for data enrichment (for example, Logstash).

#### pivoting.csv

The atc-data generates [pivoting.csv](docs/pivoting.csv) with a list of all fields (from Data Needed) mapped to description of Data Needed for very specific purpose — it provides information about data sources where some specific data type could be found, for example domain name, username, hash etc:

<details>
  <summary>Example of lookup for "hash" field (click to expand)</summary>
  <img src="images/pivoting_hash_v1.png" />
</details>

<br>

At the same time it highlights which fields could be found only with specific enrichments:

<details>
  <summary>Example of lookup for "ParentImage" field (click to expand)</summary>
  <img src="images/pivoting_parent_v1.png" />
</details>

### Requirements

- Python 3.7
- [PyYAML](https://pypi.org/project/PyYAML/), [mkdocs](https://pypi.org/project/mkdocs/) and [jinja2](https://pypi.org/project/Jinja2/) Python libraries. They could be installed with the following command:
    ```
    python3 -m pip install -r requirements.txt
    ```

## Contacts

- Folow us on [Twitter](https://twitter.com/atc_project) for updates
- Join discussions in [Slack](https://join.slack.com/t/atomicthreatcoverage/shared_invite/zt-6ropl01z-wIdiq3M0AEZPj_HiKfbiBg) or [Telegram](https://t.me/atomic_threat_coverage) 

## Contributors

Would you like to become one? You are very welcome! Our [CONTRIBUTING](CONTRIBUTING.md) guideline is a good starting point.

## Roadmap

The roadmap and related discussions could be found in the project [issues](https://github.com/atc-project/atc-data/issues).

## License

See the [LICENSE](LICENSE) file.
