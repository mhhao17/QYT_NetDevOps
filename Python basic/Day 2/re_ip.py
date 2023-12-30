import re

str1 = 'Port-channel1.189          192.168.189.254  YES     CONFIG   up'

# \w匹配字母或數字, . 匹配除換行符號以外的任意字符, \d匹配數字, \s匹配任意空白符, + 匹配前面字符一次或多次, * 匹配前面字符零次或多次
result = re.match(r'(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)',
                  str1).groups()  # 從 match object 中取得分組的值，也就是括號()裡資訊

print('-'*70)
print('%-6s : %s' % ('接口', result[0]))  # - 表示靠左對齊，6代表數值所佔寬度, s表示字符串
print('%-6s : %s' % ('IP地址', result[1]))
print('%-6s : %s' % ('狀態', result[-1]))
