import random

# 定義四個變數，分別代表四個IP位址的數字, 範圍是1~254
a = random.randint(1, 254)
b = random.randint(1, 254)
c = random.randint(1, 254)
d = random.randint(1, 254)

# 顯示四個變數的值
print(f'IPv4地址是: {a}.{b}.{c}.{d}')
