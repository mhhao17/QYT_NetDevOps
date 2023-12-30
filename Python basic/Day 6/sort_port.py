port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46',
             'eth 1/101/1/34', 'eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25',
             'eth 1/101/1/45', 'eth 1/101/2/8']

# print(sorted(port_list, key=lambda port: (int(port.split('/')[2]), int(port.split('/')[3]))))
sorted_ports = sorted(port_list, key=lambda port: (int(port.split('/')[2]), int(port.split('/')[3])))

for port in sorted_ports:
    print(port)
