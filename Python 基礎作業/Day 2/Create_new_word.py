word = input("請輸入一個單字：")
first_letter = word[0]
sub_word = word[1:]
new_word = sub_word + '-' + first_letter + 'y'
print(new_word)
