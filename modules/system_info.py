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
                6. Default Config
                7. Log
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
        
        if user_opt in ["1","2","3","4","5","6","7"] :
            self.system_info.system_command(user_opt=user_opt)
        else :
            print('Exit')

        return None

class systemInfo() :
    """
        systemInfo is a class for getting router system information.

        Include Resources, History, Clock, Router Board, and Package List.
    """
    
    def __init__(self) -> None :
        """
            initiation of object

            Define winbox system command.
        """

        self.system_info_command_list : dict = {
            "1" : "/syste resource print",
            "2" : "/system history print",
            "3" : "/system clock print",
            "4" : "/system routerboard print",
            "5" : "/system package print",
            "6" : "/system default-configuration print",
            "7" : "/log print"
        }

    def connect_to_ssh(self) -> None :
        """
            Handle ssh connection to Mikrotik Router Board.

            Use ip address that is connected to the ISP. Marked by 'D' in ip address list.

            Parameters
            ----------

            Returns
            -------
            None
        """

        self.data = sshC.connect_router()
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(username=self.data[0], password=self.data[1], hostname=self.data[2], port=22)

        return None

    def system_command(self, user_opt : str) -> None :
        """
            Run system command

            Use command that is already defined, and run the command through SSH

            Parameters
            ----------
            user_opt : str
                user choosed option in option list

            Returns
            -------
            None
        """

        self.connect_to_ssh()

        command = self.system_info_command_list[user_opt]

        stdin, stdout, stderr = self.ssh.exec_command(command)

        print(f"""
            {stdout.read().decode()}
        """)

        self.ssh.close()

        return None