import re

asa_conn = "TCP Student  192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n \
TCP Student  192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

for conn in asa_conn.split('\n'):
    result = re.match(r".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*?bytes\s+(\d+).*?flags\s+(\w*)\s*", conn).groups()
    asa_key = result[0], result[1], result[2], result[3]
    asa_value = result[4], result[5]
    asa_dict[asa_key] = asa_value

print("\n\n打印分析後的字典!\n")
print(asa_dict)

src = 'src_ip'
src_port = 'src_port'
dst = 'dst_ip   '
dst_port = 'dst_port'
bytes_name = 'bytes'
flags = 'flags'
format_str1 = '|{0:^10} : {1:^20} |{2:^10} : {3:^10} | {4:^10} : {5:^10} |{6:^10} : {7:^10}|'
format_str2 = '|{0:^10} : {1:^20} |{2:^10} : {3:^10}'

print("\n\n格式化打印输出\n")

for key, value in asa_dict.items():
    print(format_str1.format(src, key[0], src_port, key[1], dst, key[2], dst_port, key[3]))
    print(format_str2.format(bytes_name, value[0], flags, value[1]))
    print('=' * 113)
