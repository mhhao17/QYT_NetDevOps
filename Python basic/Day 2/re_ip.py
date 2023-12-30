import re

str1 = 'Port-channel1.189          192.168.189.254  YES     CONFIG   up'

result = re.match(r'(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)',
                  str1).groups()

print('-'*70)
print('%-6s : %s' % ('接口', result[0]))
print('%-6s : %s' % ('IP地址', result[1]))
print('%-6s : %s' % ('狀態', result[-1]))
