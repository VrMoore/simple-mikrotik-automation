from modules import ssh_connection as sshC
import paramiko
import os

def upload(files : str) :

    data = sshC.connect_router()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try :
        ssh.connect(username=data[0], password=data[1], hostname=data[2], port=22)
        remote_path = files.replace("\\","/")
        remote_file_name = os.path.basename(remote_path)

        sftp = ssh.open_sftp()
        sftp.put(localpath=files, remotepath=remote_file_name)

        stdin, stdout, stderr = ssh.exec_command(f'/import file-name="{remote_file_name}"')
        
        print(stdout.read().decode())
        print(stderr.read().decode())

    except Exception as e :
        print("Error : ", e)

    finally :
        sftp.close()
        ssh.close()