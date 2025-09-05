# Library
import paramiko

# Default username
username = input("Login     : ")
password = input("Password  : ")
ip_host = input("Input your client IP gateway : ")

# Create SSH Client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(ip_host, username=username, password=password)

    # Example: get system identity
    stdin, stdout, stderr = ssh.exec_command("/system identity print")

    stdin, stdout, stderr = ssh.exec_command("/ip address print")
    print(stdout.read().decode())

except Exception as e:
    print("Error:", e)
finally:
    ssh.close()