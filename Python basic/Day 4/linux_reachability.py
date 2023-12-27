import os
import re

ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
# ifconfig_result = str("""ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
#               inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
#               inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
#               ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
#               RX packets 174598769 bytes 1795658527217 (1.6 TiB)
#               RX errors 1 dropped 24662 overruns 0 frame 0
#               TX packets 51706604 bytes 41788673420 (38.9 GiB)
#               TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0""")

ipv4_add = re.findall(r'inet\s+([\d.]+)\s+', ifconfig_result)
netmask = re.findall(r'netmask\s+([\d.]+)\s+', ifconfig_result)
broadcast = re.findall(r'broadcast\s+([\d.]+)\s+', ifconfig_result)
mac_add = re.findall(r'ether\s+([0-9a-fA-F:]+)\s+', ifconfig_result)

format_string = "{0:<10}:{1:<20}"

print(format_string.format("ipv4_add", ipv4_add[0]))
print(format_string.format("netmask", netmask[0]))
print(format_string.format("broadcast", broadcast[0]))
print(format_string.format("mac_addr", mac_add[0]))

# 產生網關的IP地址，網關IP地址為ipv4_add網段的前三個IP地址+254
ipv4_gw_parts = ipv4_add[0].split('.')
ipv4_gw_parts[-1] = '254'
ipv4_gw = '.'.join(ipv4_gw_parts)

print('\n我們假設網關IP地址最後一位為254, 因此網關IP地址為:' + ipv4_gw + '\n')

# 檢查網關是否可達
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.findall(r'1 received', ping_result)

if re_ping_result:
    print('網關可達! ')
else:
    print('網關不可達! ')
