#!/usr/bin/env python3

# Import ATC classes
from scripts.dataneeded import DataNeeded
from scripts.loggingpolicy import LoggingPolicy
from scripts.enrichment import Enrichment

# Import ATC Utils
from scripts.atcutils import ATCutils

# Others
import glob
import traceback
import sys
from jinja2 import Environment, FileSystemLoader


ATCconfig = ATCutils.load_config("config.yml")

class GenerateMkdocs:
    """Class for populating mkdocs config file (navigation)"""

    def __init__(self, dn_path=False, lp_path=False, 
                 en_path=False, atc_dir=False, init=False):
        """Init"""

        # Check if atc_dir provided
        if atc_dir:
            self.atc_dir = atc_dir
        else:
            self.atc_dir = ATCconfig.get('md_name_of_root_directory') + '/'

        # Main logic

        if dn_path:
            dns, dn_paths = ATCutils.load_yamls_with_paths(dn_path)
        else:
            dns, dn_paths = ATCutils.load_yamls_with_paths(ATCconfig.get('data_needed_dir'))

        if lp_path:
            lps, lp_paths = ATCutils.load_yamls_with_paths(lp_path)
        else:
            lps, lp_paths = ATCutils.load_yamls_with_paths(ATCconfig.get('logging_policies_dir'))

        if en_path:
            ens, en_paths = ATCutils.load_yamls_with_paths(en_path)
        else:
            ens, en_paths = ATCutils.load_yamls_with_paths(ATCconfig.get('enrichments_dir'))


        dn_filenames = [dn_path.split('/')[-1].replace('.yml', '') for dn_path in dn_paths]
        lp_filenames = [lp_path.split('/')[-1].replace('.yml', '') for lp_path in lp_paths]
        en_filenames = [en_path.split('/')[-1].replace('.yml', '') for en_path in en_paths]

        # Point to the templates directory
        env = Environment(loader=FileSystemLoader('scripts/templates'))

        # Get proper template
        template = env.get_template(
            'mkdocs_config_template.yml.j2'
        )

        data_to_render = {}

        data_needed_list = []
        for i in range(len(dns)):

            dn_updated_title = dns[i].get('title')
            
            data_needed_list.append((dn_updated_title, dn_filenames[i]))
        
        logging_policy_list = []
        for i in range(len(lps)):

            rp_updated_title = lps[i].get('title')

            logging_policy_list.append((rp_updated_title, lp_filenames[i]))

        enrichment_list = []
        for i in range(len(ens)):

            en_updated_title = ens[i].get('title')
            
            enrichment_list.append((en_updated_title, en_filenames[i]))


        data_to_render.update({'data_needed_list': sorted(data_needed_list)})
        data_to_render.update({'logging_policy_list': sorted(logging_policy_list)})
        data_to_render.update({'enrichment_list': sorted(enrichment_list)})
        
        content = template.render(data_to_render)
        try:
            ATCutils.write_file('mkdocs.yml', content)
            print("[+] Created mkdocs.yml")
        except:
            print("[-] Failed to create mkdocs.yml")
        