import paramiko
import os
from modules import file_uploader as fupr
from modules import ip_lookup as ipLoo

class mainMenu :

    def __init__(self) -> None :
        print(f"""
            {'='*20}

            Welcome to Mikrotik Automation.
            Please select your option.

            1. Basic Client Internet
            2. Basic Hotspot
            3. Block Website
            4. SNMP

            8. Banner
            9. Backup

            {'='*20}

        """)

        ask_user : str = input('Opt : ')
        self.run_selected_opt(usr_opt = ask_user)

    def run_selected_opt(self, usr_opt : str) :
        curr_dir = os.getcwd()

        script_file : dict = {
            "1" : "basic_client_lan.rsc",
            "2" : "basic_hotspot.rsc",
            "3" : "block_site.rsc",
            "4" : "simple_snmp",
            "8" : "banner.rsc",
            "9" : "backup_point.rsc"
        }

                

        if usr_opt == "1" :
            local_path = os.path.join(curr_dir,"scripts","basic_client_lan.rsc")
            fupr.upload(local_path)
        elif usr_opt == "2" :
            local_path = os.path.join(curr_dir,"scripts","basic_hotspot.rsc")
            fupr.upload(local_path)
        elif usr_opt == "3" :
            local_path = os.path.join(curr_dir,"scripts","block_site.rsc")
            ipLoo.run_bash()
            fupr.upload(local_path)
        elif usr_opt == "4" :
            local_path = os.path.join(curr_dir,"scripts","simple_snmp.rsc")
            fupr.upload(local_path)
        elif usr_opt == "8" :
            local_path = os.path.join(curr_dir,"scripts","banner.rsc")
            fupr.upload(local_path)
        elif usr_opt == "9" :
            local_path = os.path.join(curr_dir,"scripts","backup_point.rsc")
            fupr.upload(local_path)
        else :
            print("Wrong input")

        

if __name__ == "__main__" :

    run_menu = mainMenu()
