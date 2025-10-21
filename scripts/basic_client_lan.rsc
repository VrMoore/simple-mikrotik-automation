# Variables
:global hostAddr "192.168.90"

# Create ip for client and ip pool
ip address add address=($hostAddr . "1/24") interface=ether2
ip pool add name=lan-pool-1 ranges=($hostAddr . ".2-" . $hostAddr . ".254")

# Create DHCP Server
ip dhcp-server network add address=($hostAddr . ".0/24") gateway=($hostAddr . ".1") 
ip dhcp-server add name=lan-dhcp interface=ether2 address-pool=lan-pool-1 disabled=no
ip dhcp-server enable lan-dhcp

# NAT
ip firewall nat add chain=srcnat action=masquerade