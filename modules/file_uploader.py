import os

import paramiko

from modules import ssh_connection as sshC

# def upload(files : str) :

#     data = sshC.connect_router()

#     self.ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#     try :
#         ssh.connect(username=data[0], password=data[1], hostname=data[2], port=22)
#         remote_path = files.replace("\\","/")
#         remote_file_name = os.path.basename(remote_path)

#         sftp = self.ssh.open_sftp()
#         sftp.put(localpath=files, remotepath=remote_file_name)

#         stdin, stdout, stderr = self.ssh.exec_command(f'/import file-name="{remote_file_name}"')

#         print(stdout.read().decode())
#         print(stderr.read().decode())

#     except Exception as e :
#         print("Error : ", e)

#     finally :
#         sftp.close()
#         ssh.close()


class Check:
    def __init__(self) -> None:
        """
        Basic config for ssh connection
        """
        self.data = sshC.connect_router()
        self.ssh = paramiko.SSHClient()

        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(
            username=self.data[0], password=self.data[1], hostname=self.data[2], port=22
        )

    def connectSftp(self, files: str) -> None:
        """
        Connect and execute file.

        Connect to mikrotik using sftp and execute given file name.

        Parameter :
        ----------
            files : str
                Given input file path from system

        Return : None
        """
        try:
            remote_path = files.replace("\\", "/")
            remote_file_name = os.path.basename(remote_path)

            sftp = self.ssh.open_sftp()
            sftp.put(localpath=files, remotepath=remote_file_name)

            stdin, stdout, stderr = self.ssh.exec_command(
                f'/import file-name="{remote_file_name}"'
            )

            print(stdout.read().decode())
            print(stderr.read().decode())

        except Exception as e:
            print("Error : ", e)

        finally:
            self.ssh.close()

    def upload(self, file_name: str) -> None:
        """
        Upload file to mikrotik

        Upload given file to mikrotik using sftp protocols.

        Parameter :
        ----------
            file_name : str
                file name of given system

        Return : None
        """
        self.connectSftp(files=file_name)

    def check_remote(self, remote_file_name: str) -> None:
        """
        Check file in mikrotik folders.

        Run check on mikrotik to check files if exist or not and print it to the terminal.

        Parameter :
        ----------
            remote_file_name : str
                Input from main.py

        Return : None
        """
        try:
            stdin, stdout, stderr = self.ssh.exec_command("/file print")

            print(stdout.read().decode())
            print(stderr.read().decode())

        except Exception as e:
            print("Error : ", e)

        finally:
            self.ssh.close()
