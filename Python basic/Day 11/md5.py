from qytang_ssh import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='Cisc0123'):
    try:
        config_raw = qytang_ssh(ip, username=username, password=password, cmd='show run')
        config = re.findall(r'hostname.*end', config_raw, re.S)[0]
        return config
    except Exception:
        return


def qytang_check_diff(ip, username='admin', password='Cisc0123'):
    before_md5 = ''
    while True:
        config = qytang_get_config(ip, username=username, password=password)
        m = hashlib.md5()
        m.update(config.encode())
        md5_value = m.hexdigest()
        if not before_md5:
            before_md5 = md5_value
        elif before_md5 != md5_value:
            print(f'配置已更改，MD5值為{md5_value}')
            break
        else:
            print(f'配置未更改，MD5值為{md5_value}')
        time.sleep(5)


if __name__ == '__main__':
    qytang_check_diff('192.168.10.101', username='admin', password='Cisc0123')
