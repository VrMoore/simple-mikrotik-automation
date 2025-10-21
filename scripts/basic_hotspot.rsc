# Global Variables
:global ipAddr "100.100.100"
:global hotspotSSID "mikrotik_hotspot"
:global hotspotPass "qwerty123"
:global hotspotDNS "bananasliced80.co.id"
:global hotspotLoginUser "user"
:global hotspotLoginPass "user"
:global userHotspotLimit 10

# wireless
interface wireless enable wlan1 
interface wireless security-profiles add name=prof1 mode=dynamic-keys authentication-types=wpa-psk,wpa2-psk wpa-pre-shared-key=$hotspotPass wpa2-pre-shared-key=$hotspotPass
interface wireless set numbers=wlan1 mode=ap-bridge band=2ghz-b/g/n ssid=$hotspotSSID radio-name=$hotspotSSID security-profile=prof1 disabled=no

# Create ip address and pool
ip address add address=($ipAddr . ".1/24") interface=wlan1
ip pool add name=hs-pool-1 ranges=($ipAddr . ".2-" . $ipAddr . ".254")

# Create DHCP Server
ip dhcp-server network add address=($ipAddr . ".0/24") gateway=($ipAddr . ".1") dns-server=8.8.8.8
ip dhcp-server add name=hs-dhcp interface=wlan1 address-pool=hs-pool-1 disabled=no
ip dhcp-server enable hs-dhcp

# Create hotspot server
ip hotspot profile add name=hsprof1 hotspot-address=($ipAddr . ".1") dns-name=$hotspotDNS html-directory=hotspot html-directory-override="" rate-limit="" http-proxy=0.0.0.0:0 smtp-server=0.0.0.0 login-by=cookie,http-chap http-cookie-lifetime=3d split-user-domain=no use-radius=no
ip hotspot add name=server1 profile=hsprof1 interface=wlan1 address-pool=hs-pool-1 disabled=no

# Create user
ip hotspot user profile add name=uprof1 shared-users=$userHotspotLimit
ip hotspot user add name=$hotspotLoginUser password=$hotspotLoginPass profile=uprof1 

put "Hotspot setup complete"