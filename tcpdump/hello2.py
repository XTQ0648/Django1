import re

residents = '420111199808120045,420105197905230034,420107198504140023,42010320010726007X'

for resident in residents.split(','):
    id_num = resident[:18]
    birth = id_num[6:14]
    gender = '男' if int(id_num[-2]) % 2 == 1 else '女'
    print(f'身份证号码：{id_num}，出生日期：{birth[:4]}年{birth[4:6]}月{birth[6:]}日，性别：{gender}')
