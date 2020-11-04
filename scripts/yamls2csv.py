#!/usr/bin/env python3

from scripts.datautils import DATAutils
from scripts.attack_mapping import te_mapping, ta_mapping
from pathlib import Path

import csv
import sys
import getopt
from os import listdir
from os.path import isfile, join
from yaml.scanner import ScannerError

ATCconfig = DATAutils.load_config("config.yml")

HELP_MESSAGE = """Usage: python3 yamls2csv.py [OPTIONS]\n\n\n
\t\tPossible options are --detectionrules_path, --dataneeded_path
--loggingpolicies path
\t\tDefaults are
\t\tdataneeded_path = ../data_needed/;
\t\tloggingpolicies_path=../logging_policies/"""

class GenerateCSV:

    def __init__(self):

        dn_path = ATCconfig.get('data_needed_dir')
        lp_path = ATCconfig.get('logging_policies_dir')
        en_path = ATCconfig.get('enrichments_dir')

        dn_list = DATAutils.load_yamls(dn_path)
        lp_list = DATAutils.load_yamls(lp_path)
        enrichments_list = DATAutils.load_yamls(en_path)

        pivoting = []
        analytics = []
        result = []

        analytics = []

        for dn in dn_list:

            if 'category' in dn:
                dn_category = dn['category']
            else:
                dn_category = "-"
            if 'platform' in dn:
                dn_platform = dn['platform']
            else:
                dn_platform = "-"
            if 'type' in dn:
                dn_type = dn['type']
            else:
                dn_type = "-"
            if 'channel' in dn:
                dn_channel = dn['channel']
            else:
                dn_channel = "-"
            if 'provider' in dn:
                dn_provider = dn['provider']
            else:
                dn_provider = "-"
            if 'title' in dn:
                dn_title = dn['title']
            else:
                dn_title = "-"

            pivot = [dn_category, dn_platform, dn_type,
                     dn_channel, dn_provider, dn_title, '', '']
            for field in dn['fields']:
                analytics.append([field] + pivot)

        for er in enrichments_list:
            for dn in [dnn for dnn in dn_list if dnn['title'] in er.get(
                    'data_to_enrich', [])]:
                pivot = [
                    dn['category'], dn['platform'], dn['type'], dn['channel'],
                    dn['provider'], dn['title'], er['title'],
                    ';'.join(er.get('requirements', []))
                ]
                for field in er['new_fields']:
                    analytics.append([field] + pivot)

        filename = 'pivoting.csv'
        exported_analytics_directory = ATCconfig.get(
            'exported_analytics_directory'
        )

        Path(exported_analytics_directory).mkdir(parents=True, exist_ok=True)

        with open(
            exported_analytics_directory + '/' + filename, 'w',
                newline='') as csvfile:
            # maybe need some quoting
            alertswriter = csv.writer(csvfile, delimiter=',')
            alertswriter.writerow([
                'field', 'category', 'platform', 'type', 'channel', 'provider',
                'data_needed', 'enrichment', 'enrichment requirements'
            ])
            for row in analytics:
                alertswriter.writerow(row)

        print(f'[+] Created {filename}')
