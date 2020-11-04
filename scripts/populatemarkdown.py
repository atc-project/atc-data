#!/usr/bin/env python3

# Import ATC classes
try:
    from scripts.dataneeded import DataNeeded
    from scripts.loggingpolicy import LoggingPolicy
    from scripts.enrichment import Enrichment
    from scripts.datautils import DATAutils
    from scripts.init_markdown import create_markdown_dirs
except:
    from data.atc_data.scripts.dataneeded import DataNeeded
    from data.atc_data.scripts.loggingpolicy import LoggingPolicy
    from data.atc_data.scripts.enrichment import Enrichment
    from data.atc_data.scripts.datautils import DATAutils
    from data.atc_data.scripts.init_markdown import create_markdown_dirs

# Others
import glob
import traceback
import sys
import subprocess

ATCconfig = DATAutils.load_config("config.yml")


class DataPopulateMarkdown:
    """Class for populating markdown repo"""

    def __init__(self, lp=False, dn=False, en=False, auto=False,
                 atc_dir=False, lp_path=False, dn_path=False,
                 en_path=False, init=False):
        """Init"""

        # Check if atc_dir provided
        if atc_dir:
            self.atc_dir = atc_dir

        else:
            self.atc_dir = ATCconfig.get('md_name_of_root_directory') + '/'

        # Check if init switch is used
        if init:
            if self.init_export():
                print("[+] Created initial DATA markdown directories successfully")
            else:
                print("[-] Failed to create initial markdown directories")
                raise Exception("Failed to markdown directories")

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

    def init_export(self):
        try:
            create_markdown_dirs()
            return True
        except:
            return False

    def logging_policy(self, lp_path):
        """Populate Logging Policies"""

        print("[*] Populating Logging Policies...")
        if lp_path:
            lp_list = glob.glob(lp_path + '*.yml')
        else:
            lp_dir = ATCconfig.get('logging_policies_dir')
            lp_list = glob.glob(lp_dir + '/*.yml')

        for lp_file in lp_list:
            try:
                lp = LoggingPolicy(lp_file)
                lp.render_template("markdown")
                lp.save_markdown_file(atc_dir=self.atc_dir)
            except Exception as e:
                print(lp_file + " failed\n\n%s\n\n" % e)
                print("Err message: %s" % e)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)

        print("[+] Logging Policies populated!")

    def data_needed(self, dn_path):
        """Populate Data Needed"""

        print("[*] Populating Data Needed...")
        if dn_path:
            dn_list = glob.glob(dn_path + '*.yml')
        else:
            dn_dir = ATCconfig.get('data_needed_dir')
            dn_list = glob.glob(dn_dir + '/*.yml')

        for dn_file in dn_list:
            try:
                dn = DataNeeded(dn_file)
                dn.render_template("markdown")
                dn.save_markdown_file(atc_dir=self.atc_dir)
            except Exception as e:
                print(dn_file + " failed\n\n%s\n\n" % e)
                print("Err message: %s" % e)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
        print("[+] Data Needed populated!")

    def enrichment(self, en_path):
        """Populate Enrichments"""

        print("[*] Populating Enrichments...")
        if en_path:
            en_list = glob.glob(en_path + '*.yml')
        else:
            en_dir = ATCconfig.get('enrichments_dir')
            en_list = glob.glob(en_dir + '/*.yml')

        for en_file in en_list:
            try:
                en = Enrichment(en_file)
                en.render_template("markdown")
                en.save_markdown_file(atc_dir=self.atc_dir)
            except Exception as e:
                print(en_file + " failed\n\n%s\n\n" % e)
                print("Err message: %s" % e)
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
        print("[+] Enrichments populated!")
