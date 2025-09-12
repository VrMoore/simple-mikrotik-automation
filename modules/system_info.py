from modules import ssh_connection as sshC
import time
import paramiko

# Get router system information

class systemMenu() :

    def __init__(self) :
        self.system_info = systemInfo()
        self.menu()

    def menu(self) :
        print(f"""
        ----------------------------------
            Select system info :

                1. Resources
                2. History
                3. Clock
                4. Router Board
                5. Package List
        ----------------------------------
        """)
        
        ask_user = input("Choose : ")
        self.run_chosen_program(user_opt=ask_user)

    def run_chosen_program(self, user_opt : str) :
        
        if user_opt == "1" :
            self.system_info.resources_info()
        elif user_opt == "2" :
            self.system_info.system_history_info()
        elif user_opt == "3" :
            self.system_info.system_clock_info()
        elif user_opt == "4" :
            self.system_info.system_router_board_info()
        elif user_opt == "5" :
            self.system_info.system_package_list_info()
        else :
            print("EXIT")

class systemInfo() :
    """
        systemInfo is a class for getting router system information.

        Handle resources, cpu load, etc.
    """
    
    def __init__(self) :
        pass

    def connect_to_ssh(self) :
        self.data = sshC.connect_router()
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(username=self.data[0], password=self.data[1], hostname=self.data[2], port=22)

    def resources_info(self) :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system resource print")
        print(stdout.read().decode())

        self.ssh.close()

    def system_history_info(self) :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system history print")
        print(stdout.read().decode())

        self.ssh.close()

    def system_clock_info(self) :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system clock print")
        print(stdout.read().decode())

        self.ssh.close()

    def system_router_board_info(self) :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system routerboard print")
        print(stdout.read().decode())

        self.ssh.close()

    def system_package_list_info(self) :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system package print")
        print(stdout.read().decode())

        self.ssh.close()

