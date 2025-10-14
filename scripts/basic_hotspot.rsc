# wireless
interface wireless enable wlan1 
interface wireless security-profiles add name=prof1 mode=dynamic-keys authentication-types=wpa-psk,wpa2-psk wpa-pre-shared-key=qwerty123 wpa2-pre-shared-key=qwerty123
interface wireless set numbers=wlan1 mode=ap-bridge band=2ghz-b/g/n ssid=mikrotik_hotspot radio-name=mikrotik_hotspot security-profile=prof1 disabled=no

# Create ip address and pool
ip address add address=100.100.100.1/24 interface=wlan1
ip pool add name=hs-pool-1 ranges=100.100.100.2-100.100.100.254 

# Create DHCP Server
ip dhcp-server network add address=100.100.100.0/24 gateway=100.100.100.1 dns-server=8.8.8.8
ip dhcp-server add name=hs-dhcp interface=wlan1 address-pool=hs-pool-1 disabled=no
ip dhcp-server enable hs-dhcp

ip hotspot profile add name=hsprof1 hotspot-address=100.100.100.1 dns-name="slicedbanana80.co.id" html-directory=hotspot html-directory-override="" rate-limit="" http-proxy=0.0.0.0:0 smtp-server=0.0.0.0 login-by=cookie,http-chap http-cookie-lifetime=3d split-user-domain=no use-radius=no
ip hotspot add name=server1 profile=hsprof1 interface=wlan1 address-pool=hs-pool-1 disabled=no

# Create user
ip hotspot user profile add name=uprof1 shared-users=10
ip hotspot user add name=user password=user profile=uprof1 

put "Hotspot setup complete"