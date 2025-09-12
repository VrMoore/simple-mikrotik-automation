# SIMPLE MIKROTIK AUTOMATION USING PARAMIKO

<b>[Paramiko](https://github.com/paramiko/paramiko?tab=readme-ov-file)</b> is a Python Library that implement SSHv2 providing both client and server functionality.

First, install paramiko library with following command.
`
	python -m pip install paramiko
`
## Step by Step to Setup Mikrotik
In order the make the code run, you need to ensure you already have setup mikrotik by following step.

1. Open Winbox and select your Mikrotik
2. Open the terminal
3. Type following commands :
	>	ip dhcp-client add interface=.... disabled=no
	>	ip address add address=.../... interface=...
	> ip dhcp-server setup
	> ip firewall nat add chain=srcnat action=masquerade

## How to run the program
1. Type `ip address print` in the winbox terminal
2. Run the program, on the `ip address` question, enter the one that you see with the letter <b>D</b> (Dynamic).

### Footnote
--