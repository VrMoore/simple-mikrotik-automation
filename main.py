import paramiko
import os
from modules import file_uploader as fupr

class mainMenu :

    def __init__(self) -> None :
        print(f"""
            {'='*20}

            Welcome to Mikrotik Automation.
            Please select your option.

            1. Basic Hotspot
            2. Block Website
            3. SNMP

            {'='*20}

        """)

        ask_user : str = input('Opt : ')
        self.run_selected_opt(usr_opt = ask_user)

    def run_selected_opt(self, usr_opt : str) :
        curr_dir = os.getcwd()

        if usr_opt == "1" :
            local_path = os.path.join(curr_dir,"scripts","basic_hotspot.rsc")
            fupr.upload(local_path)
        elif usr_opt == "2" :
            local_path = os.path.join(curr_dir,"scripts","block_site.rsc")
            fupr.upload(local_path)
        elif usr_opt == "3" :
            local_path = os.path.join(curr_dir,"scripts","simple_snmp.rsc")
            fupr.upload(local_path)
        else :
            print("Wrong input")

        

if __name__ == "__main__" :

    run_menu = mainMenu()
