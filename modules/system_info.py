from modules import ssh_connection as sshC
import time
import paramiko

class systemMenu() :
    """
        systemMenu handle menu information of user selection of choice.

        Selection of choice included in this class are; 
        Resources, History, CLock, Router Board, and Package List.
    """

    def __init__(self) :
        """
            initiation of object

            run system info by calling the object and systemMenu menu.
        """

        self.system_info = systemInfo()
        self.menu()

    def menu(self) :
        """
            Show selection of choices
        """

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

        return 

    def run_chosen_program(self, user_opt : str) -> None :
        """
            Run choosen program based on user choices.

            Parameters
            ----------
            user_opt : str
                user selected option in menu

            Returns
            -------
            None
        """
        
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

        return 

class systemInfo() :
    """
        systemInfo is a class for getting router system information.

        Include Resources, History, Clock, Router Board, and Package List.
    """
    
    def __init__(self) -> None :
        """
            Initiation of object
        """
        pass

    def connect_to_ssh(self) -> None :
        """
            Handle ssh connection to Mikrotik Router Board.

            Use ip address that is connected to the ISP. Marked by 'D' in ip address list.
        """

        self.data = sshC.connect_router()
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(username=self.data[0], password=self.data[1], hostname=self.data[2], port=22)

        return None

    def resources_info(self) -> None :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system resource print")
        print(stdout.read().decode())

        self.ssh.close()

        return None

    def system_history_info(self) -> None :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system history print")
        print(stdout.read().decode())

        self.ssh.close()

        return None

    def system_clock_info(self) -> None :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system clock print")
        print(stdout.read().decode())

        self.ssh.close()

        return None

    def system_router_board_info(self) -> None:
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system routerboard print")
        print(stdout.read().decode())

        self.ssh.close()

        return None

    def system_package_list_info(self) -> None :
        self.connect_to_ssh()

        stdin, stdout, stderr = self.ssh.exec_command("/system package print")
        print(stdout.read().decode())

        self.ssh.close()

        return None


# Make a dictionary that list of all selected command

# data = {
#     1 : 'sy'
# }