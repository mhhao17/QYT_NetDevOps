import re

str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

result = re.match(r'(\d+)\s+([0-9a-fa-f]{4}\.[0-9a-fa-f]{4}\.[0-9a-fa-f]{4})\s+(\w+)\s+(\S+)', str1).groups()

print('%-10s : %s' % ('VLAN ID', result[0]))
print('%-10s : %s' % ('MAC', result[1]))
print('%-10s : %s' % ('Type', result[-2]))
print('%-10s : %s' % ('Interface', result[-1]))
