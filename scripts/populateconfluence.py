#!/usr/bin/env python3

# Import ATC classes
try:
    from scripts.dataneeded import DataNeeded
    from scripts.loggingpolicy import LoggingPolicy
    from scripts.enrichment import Enrichment
except:
    from data.atc_data.scripts.dataneeded import DataNeeded
    from data.atc_data.scripts.loggingpolicy import LoggingPolicy
    from data.atc_data.scripts.enrichment import Enrichment

# Import ATC Utils
from scripts.atcutils import ATCutils
from scripts.init_confluence import main as init_main

# Others
import glob
import sys
import traceback
import os

ATCconfig = ATCutils.load_config("config.yml")


class DataPopulateConfluence:
    """Desc"""

    def __init__(self, auth, lp=False, dn=False, en=False,
                 auto=False, atc_dir=False, lp_path=False,
                 dn_path=False, en_path=False, init=False):
        """Desc"""

        self.auth = auth

        self.space = ATCconfig.get('confluence_space_name')
        self.apipath = ATCconfig.get('confluence_rest_api_url')
        self.root_name = ATCconfig.get('confluence_name_of_root_directory')

        # Check if atc_dir provided
        if atc_dir:
            self.atc_dir = atc_dir

        else:
            self.atc_dir = ATCconfig.get('md_name_of_root_directory')

        # Check if init switch is used
        if init:
            if init_main(self.auth):
                print("[+] Created initial confluence pages successfully")
            else:
                print("[-] Failed to create initial confluence pages")
                raise Exception("Failed to init pages")

        # Main logic
        if auto:
            self.logging_policy(lp_path)
            self.data_needed(dn_path)
            self.enrichment(en_path)
        
        if lp:
            self.logging_policy(lp_path)

        if dn:
            self.data_needed(dn_path)

        if en:
            self.enrichment(en_path)

    def logging_policy(self, lp_path):
        """Desc"""

        print("[*] Populating Logging Policies...")
        if lp_path:
            lp_list = glob.glob(lp_path + '*.yml')
        else:
            lp_dir = ATCconfig.get('logging_policies_dir')
            lp_list = glob.glob(lp_dir + '/*.yml')

        for lp_file in lp_list:
            try:
                lp = LoggingPolicy(lp_file)
                lp.render_template("confluence")
                confluence_data = {
                    "title": lp.fields["title"],
                    "spacekey": self.space,
                    "parentid": str(ATCutils.confluence_get_page_id(
                        self.apipath, self.auth, self.space,
                        "Logging Policies")),
                    "confluencecontent": lp.content,
                }

                res = ATCutils.push_to_confluence(confluence_data, self.apipath,
                                            self.auth)
                if res == 'Page updated':
            	    print("==> updated page: LP '" + lp.fields['title'] + "'")
                # print("Done: ", lp.fields['title'])
            except Exception as err:
                print(lp_file + " failed")
                print("Err message: %s" % err)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
        print("[+] Logging Policies populated!")

    def data_needed(self, dn_path):
        """Desc"""

        print("[*] Populating Data Needed...")
        if dn_path:
            dn_list = glob.glob(dn_path + '*.yml')
        else:
            dn_dir = ATCconfig.get('data_needed_dir')
            dn_list = glob.glob(dn_dir + '/*.yml')

        for dn_file in dn_list:
            try:
                dn = DataNeeded(dn_file, apipath=self.apipath, auth=self.auth,
                                space=self.space)
                dn.render_template("confluence")
                confluence_data = {
                    "title": dn.dn_fields["title"],
                    "spacekey": self.space,
                    "parentid": str(ATCutils.confluence_get_page_id(
                        self.apipath, self.auth, self.space, "Data Needed")),
                    "confluencecontent": dn.content,
                }

                res = ATCutils.push_to_confluence(confluence_data, self.apipath,
                                            self.auth)
                if res == 'Page updated':
            	    print("==> updated page: DN '" + dn.dn_fields['title'] + "'")
                # print("Done: ", dn.dn_fields['title'])
            except Exception as err:
                print(dn_file + " failed")
                print("Err message: %s" % err)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
        print("[+] Data Needed populated!")

    def enrichment(self, en_path):
        """Nothing here yet"""

        print("[*] Populating Enrichments...")
        if en_path:
            en_list = glob.glob(en_path + '*.yml')
        else:
            en_dir = ATCconfig.get('enrichments_directory')
            en_list = glob.glob(en_dir + '/*.yml')

        for en_file in en_list:
            try:
                en = Enrichment(en_file, apipath=self.apipath,
                                auth=self.auth, space=self.space)
                en.render_template("confluence")

                confluence_data = {
                    "title": en.en_parsed_file['title'],
                    "spacekey": self.space,
                    "parentid": str(ATCutils.confluence_get_page_id(
                        self.apipath, self.auth, self.space,
                        "Enrichments")), "confluencecontent": en.content,
                }

                res = ATCutils.push_to_confluence(confluence_data, self.apipath,
                                            self.auth)
                if res == 'Page updated':
            	    print("==> updated page: EN '" + en.en_parsed_file['title'] + "'")
                # print("Done: ", en.en_parsed_file['title'])
            except Exception as err:
                print(en_file + " failed")
                print("Err message: %s" % err)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
        print("[+] Enrichments populated!")
