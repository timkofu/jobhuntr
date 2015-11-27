#!/bin/bash

iptables -F

iptables -A INPUT -s 127.0.0.1 -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# SSH DOS
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set --name SSH -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -m recent --update --seconds 3600 --hitcount 4 --rttl --name SSH -j DROP

# HTTPD DOS
iptables -A INPUT -p tcp --dport 80 -m state --state NEW -m limit --limit 50/minute --limit-burst 200 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -m state --state RELATED,ESTABLISHED -m limit --limit 50/second --limit-burst 50 -j ACCEPT

#iptables -A INPUT -p tcp --dport 80 -j ACCEPT

#iptables -A INPUT -p icmp --icmp-type 8 -j ACCEPT
iptables -A INPUT -j DROP


