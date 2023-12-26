import re

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 00:01:09, bytes 27575949, flags UIO'

result = re.match(r'(TCP)\s+server\s+(?P<server>[\d.]+:\d+)\s+localserver\s+(?P<local>[\d.]+:\d+),\s+idle\s+(?P<idle>[\d:]+),\s+bytes\s+(?P<bytes>\d+),\s+flags\s+(?P<flags>\w+)', str1).groups()

idle_parts = result[3].split(':')
hours, minutes, seconds = map(int, idle_parts)

idle_formatted = '{:02} 小時 {:02}分鐘 {:02}秒'.format(hours, minutes, seconds)

if hours < 10:
    idle_formatted = '{} 小時 {:02}分鐘 {:02}秒'.format(hours, minutes, seconds)
else:
    idle_formatted = '{:02} 小時 {:02}分鐘 {:02}秒'.format(hours, minutes, seconds)

print('%-11s : %s' % ('protocol', result[0]))
print('%-11s : %s' % ('server', result[1]))
print('%-11s : %s' % ('localserver', result[2]))
print('%-11s : %s' % ('idle', idle_formatted))
print('%-11s : %s' % ('bytes', result[4]))
print('%-11s : %s' % ('flags', result[5]))
