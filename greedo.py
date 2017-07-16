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

fix = "echo && apt remove resolvconf -y && echo && /etc/init.d/networking restart && echo && apt-get install resolvconf -y"

print "[!] Fixing shitty resolvconf..."
os.system(fix)
print "\t[*] Fixed..."
print "[!] Launching test page..."

testfix = "firefox http://starwars.wikia.com/wiki/Greedo"
os.system(testfix)
