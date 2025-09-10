from modules import ssh_connection as sshC
import time
import paramiko

# Get router system information

class systemInfo() :
    """
        systemInfo is a class for getting router system information.

        Handle resources, cpu load, etc.
    """
    
    def __init__(self) :
        self.resources_info()

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



if __name__ == "__main__" :
    test = systemInfo()
    test.resources_info()

