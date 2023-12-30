'''
功能 : 輸入一個單字並重新自創一個新單字
'''

word = input("請輸入一個單字：")

# 將所輸入單字的index 0 放置變數 first_letter
first_letter = word[0]

# 將index 1之後的字串放置變數 sub_word
sub_word = word[1:]

# 重新合併字串
new_word = sub_word + '-' + first_letter + 'y'

# 輸出合併完成的字串 new_word
print(new_word)
