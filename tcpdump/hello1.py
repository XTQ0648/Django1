word = "111111111111222222222222233333333333333"
str1 = "_"
findstr = word[0] + word[2:4] + word[-3:-1]
#
print(word.split("1", 2))
# 分割：以_分割word
print(str1.join(word))
# 替换：f->1，1个
print(word.replace('f', '1', 1))
# 查找：从8开始15结束查找111
print(word.find("111", 8, 15))
