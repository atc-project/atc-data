#!/usr/bin/env python3

from scripts.atcutils import ATCutils

from scripts.populatemarkdown import DataPopulateMarkdown
from scripts.populateconfluence import DataPopulateConfluence
from scripts.yamls2csv import GenerateCSV
from scripts.generate_mkdocs_config import GenerateMkdocs

# For confluence
from requests.auth import HTTPBasicAuth

# Others
import argparse
import getpass
import random
import string
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="""Main function of ATC Data.

    You can not only choose to export analytics but also to use different
    modules.
""")

    # Mutually exclusive group for chosing the output of the script
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-C', '--confluence', action='store_true',
                       help='Export analytics to Confluence')
    group.add_argument('-M', '--markdown', action='store_true',
                       help='Export analytics to Markdown repository')
    group.add_argument('-Y2C', '--yaml-to-csv', action='store_true',
                       help='Generate a CSV file out of yaml files')
    group.add_argument('-MK', '--mkdocs', action='store_true',
                       help='Generate mkdocs navigation file')


    # Mutually exclusive group for chosing type of data
    group2 = parser.add_mutually_exclusive_group(required=False)

    group2.add_argument('-A', '--auto', action='store_true',
                        help='Build full repository')
    group2.add_argument('-LP', '--loggingpolicy', action='store_true',
                        help='Build logging policy part')
    group2.add_argument('-DN', '--dataneeded', action='store_true',
                        help='Build data needed part')
    group2.add_argument('-EN', '--enrichment', action='store_true',
                        help='Build enrichment part')

    # Init capabilities
    parser.add_argument('-i', '--init', action='store_true',
                        help="Build initial pages or directories " +
                        "depending on the export type")

    args = parser.parse_args()

    if args.markdown:
        DataPopulateMarkdown(auto=args.auto, lp=args.loggingpolicy,
                         dn=args.dataneeded,en=args.enrichment,
                         init=args.init)

    elif args.confluence:
        print("Provide Confluence credentials\n")

        mail = input("Login: ")
        password = getpass.getpass(prompt='Password: ', stream=None)

        auth = HTTPBasicAuth(mail, password)
        DataPopulateConfluence(auth=auth, auto=args.auto, lp=args.loggingpolicy,
                           dn=args.dataneeded,en=args.enrichment,
                           init=args.init)

    elif args.yaml_to_csv:
        GenerateCSV()
    
    elif args.mkdocs:
        GenerateMkdocs()
