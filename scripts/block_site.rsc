
ip firewall address-list add list=BlockedWebsites address=31.13.95.35 comment="www.facebook.com"
ip firewall filter add chain=forward dst-address-list=BlockedWebsites action=drop
