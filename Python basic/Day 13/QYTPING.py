from kamene.all import *


class QYTPING:
    def __init__(self, ip):
        self.srcip = None
        self.dstip = ip
        self.pkt = IP(dst=self.dstip, src=self.srcip)/ICMP()
        self.length = 100

    def src(self, srcip):
        self.srcip = srcip
        self.pkt = IP(dst=self.dstip, src=self.srcip)/ICMP()

    def one(self):
        result = sr1(self.pkt, timeout=2, verbose=False)
        if result:
            print(self.dstip,  ' 可達!')
        else:
            print(self.dstip,  ' 不可達!')

    def ping(self):
        for i in range(0, 5):
            result = sr1(self.pkt, timeout=2, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()

    def __str__(self):
        if self.srcip:
            return '<{0} => srcip: {1}, dstip: {2}, size: {3}>'.format(
                self.__class__.__name__,
                self.srcip,
                self.dstip,
                self.length
            )
        else:
            return '<{0} => dstip: {1}, size: {2}>'.format(
                self.__class__.__name__,
                self.dstip,
                self.length
            )


class NewPing(QYTPING):
    def ping(self):
        for i in range(0, 5):
            result = sr1(self.pkt, timeout=2, verbose=False)
            if result:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)
        print()


if __name__ == '__main__':
    ping = QYTPING('192.168.10.254')  # 使用class QTYPING,產生實例
    total_len = 70


    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word)) / 2), word, s * int((70 - len(word)) / 2)))


    print_new('print class')
    print(ping)  # 列印class
    print_new('ping one for sure reachable')
    ping.one()  # Ping 一個包判斷可達性
    print_new('ping five')
    ping.ping()  # 模擬正常程序ping五個包, '!'表示通, '.'表示不通
    print_new('set payload lenth')
    ping.length = 200  # 設定payload長度
    print(ping)  # 列印class
    ping.ping()  # 使用新的payload長度ping測試
    print_new('set ping src ip address')
    ping.srcip = '192.168.10.123'  # 修改源IP地址
    print(ping)  # 列印class
    ping.ping()  # 使用修改長度又修改源的包進行ping測試
    print_new('new class NewPing', '=')  # 這裡是使用繼承的方式, 產生新的class
    newping = NewPing('192.168.10.254')  # 使用class NewPing(通過繼承QYTPING class)產生實例
    newping.length = 300
    print(newping)  # 列印class
    newping.ping()  # NewPing class自訂義ping()這個方法, '+'表示通, '?'表示不通

