"""
格式化字串練習
"""
# 將字串及數值放進變數
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

# 格式化字符串, %-10s 表示插入一個字符串（s），並向左對齊(-)，總寬度為10，代表兩個字串中間空幾格。
# 格式化字符串, %-10.2f 表示插入一個浮點數（f），總寬度為10個字符，其中包括小數點和小數點後兩位。
# line1 = ('Department1 name:%-10s  Manager:%-10s  COURSE FEES:%-10.2f  The End!'
#          % (department1, depart1_m, COURSE_FEES_SEC))
# line2 = ('Department2 name:%-10s  Manager:%-10s  COURSE FEES:%-10.2f  The End!'
#          % (department2, depart2_m, COURSE_FEES_Python))
# {0:<10}, < 左對齊，總寬度為10個字符。0是參數的索引，表示插入第一個參數（department1）
line1 = ('Department1 name:{0:<10}  Manager:{1:<10}  COURSE FEES:{2:<10.2f}  '
         'The End!'.format(department1, depart1_m, COURSE_FEES_SEC))
line2 = ('Department2 name:{0:<10}  Manager:{1:<10}  COURSE FEES:{2:<10.2f}  '
         'The End!'.format(department2, depart2_m, COURSE_FEES_Python))

# 計算line1的長度
length = len(line1)

print('=' * length)
print(line1)
print(line2)
print('=' * length)
