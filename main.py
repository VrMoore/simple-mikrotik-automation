import os
from unittest.main import TestProgram

import paramiko

from modules import file_uploader as fupr
from modules import ip_lookup as ipLoo


class mainMenu:
    """
    MainMenu for Mikrotik Apps
    """

    def __init__(self) -> None:
        """
        Basic option for mikrotik applications.

        Parameter : None
        Return : None
        """

        self.file_tool = fupr.Check()

        print(f"""
            {"=" * 20}

            Welcome to Mikrotik Automation.
            Please select your option.

            1. Basic Client Internet
            2. Basic Hotspot
            3. Block Website
            4. SNMP

            8. Banner
            9. Backup

            {"=" * 20}

        """)

        ask_user: str = input("Opt : ")
        self.run_selected_opt(usr_opt=ask_user)

    def run_selected_opt(self, usr_opt: str) -> None:
        """
        Run selected user option.

        Automatically send banner once if already banner in mikrotik. Banner is custom made by me, you can customize it by yourself.

        Parameter :
        ----------
            usr_opt : str
                Input from self.innit

        Return : None
        """

        # Get current working directory
        curr_dir = os.getcwd()

        # List name of file for easier file execution
        script_file: dict = {
            "1": "basic_client_lan.rsc",
            "2": "basic_hotspot.rsc",
            # "3": "block_site.rsc",
            "4": "simple_snmp",
            "9": "backup_point.rsc",
        }

        banner_file = "banner.rsc"
        # Check file in mikrotik
        check_exist = self.file_tool.check_remote(banner_file)
        print("===", check_exist, "===")

        # Handle user option
        if usr_opt in script_file:
            local_path = os.path.join(curr_dir, "scripts", script_file[usr_opt])
            test_path = f"{local_path}.rsc"
            print(test_path)

            if usr_opt == "4":
                ipLoo.run_bash()

            self.file_tool.upload(file_name=test_path)

        else:
            print("Wrong input")


if __name__ == "__main__":
    run_menu = mainMenu()
