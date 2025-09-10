from modules import ssh_connection as sshC
import paramiko
import time

# Automate hotspot setup
class hotspotSetup() :
    """
        Auto setup for hotspot

        Handle Hotspot Setup, DNS Name, Users, and User Profiles.
    """

    def __init__(self) :
        print("Hotspot Automation")

        self.connect_to_ssh()

    def connect_to_ssh(self) :
        data = sshC.connect_router()

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(username=data[0], password=data[1], hostname=data[2], port=22)

            stdin, stdout, stderr = ssh.exec_command("/system identity print")

            print(stdout.read().decode())

        except Exception as e:
            print("Error:", e)

        finally:
            ssh.close()

if __name__ == "__main__" :
    test = hotspotSetup()
    test.connect_to_ssh()

# # Hotspot parameters
# interface = "ether2"
# hotspot_ip = "192.168.10.1/24"
# dns_name = "hotspot.local"
# profile_name = "hsprof1"
# server_name = "hotspot1"
# user_profile = "basic"
# user_name = "test"
# user_pass = "123"

# commands = [
#     # 1. Add IP address on LAN interface
#     f"/ip address add address={hotspot_ip} interface={interface}",

#     # 2. Create hotspot profile
#     f"/ip hotspot profile add name={profile_name} hotspot-address={hotspot_ip.split('/')[0]} dns-name={dns_name}",

#     # 3. Create hotspot server
#     f"/ip hotspot add name={server_name} interface={interface} profile={profile_name}",

#     # 4. Create user profile
#     f"/ip hotspot user profile add name={user_profile} rate-limit=2M/2M",

#     # 5. Create user
#     f"/ip hotspot user add name={user_name} password={user_pass} profile={user_profile}"
# ]

# # Use interactive shell to push sequential commands
# shell = ssh.invoke_shell()
# for cmd in commands:
#     shell.send(cmd + "\n")
#     time.sleep(1)  # give router time to apply command

# # Grab output
# time.sleep(2)
# output = shell.recv(5000).decode()
# print(output)

# ssh.close()
# print("✅ Hotspot setup complete")
