#!/usr/bin/python

'''
Quick n' dirty DNS resolvconf fix
'''

import os
print "[!] Killing target creature... openvpn"
find = "ps -aux | grep -i openvpn | grep -vi grep"
find2 = os.popen(find).read()
if find2:
    kill = "kill -9 " + find2.split()[1]
    os.system(kill)
    print "\t[*] Found and killed Openvpn... now where's my bounty?!"
else:
    pass

fix1 = "apt remove resolvconf -y"
fix2 = "/etc/init.d/networking restart"
fix3 = "apt-get install resolvconf -y"
sep = " && "

print "[!] Fixing shitty resolvconf..."
chain = fix1 + sep + fix2 + sep + fix3
os.system(chain)
print "\t[*] Fixed..."
print "[!] Launching test page..."

testfix = "firefox http://starwars.wikia.com/wiki/Greedo"
os.system(testfix)
