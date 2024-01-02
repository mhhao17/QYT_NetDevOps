import os
import time

while True:
    monitor_http = os.popen('netstat -tulnp').read()

    monitor_socket_list = monitor_http.split('\n')
    monitor_socket_list = monitor_socket_list[2:-1]

    for http_port in monitor_socket_list:
        if http_port.split()[3].split(':')[-1] == '80':
            print('HTTP (TCP/80) 服務已經被打開')
            break
    else:
        print('等待一秒重新開始監控')
        time.sleep(1)
        continue
    break


