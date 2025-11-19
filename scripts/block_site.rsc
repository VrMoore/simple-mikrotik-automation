
ip firewall address-list add list=BlockedWebsites address=157.240.208.35 comment="www.facebook.com"
ip firewall filter add chain=forward dst-address-list=BlockedWebsites action=drop
