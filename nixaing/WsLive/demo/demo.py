# from v1_pb2 import Person, Message
#
# p1 = Person()
# p1.name = "wupeiqi"
# p1.age = 29
# info = p1.SerializeToString()
# print(info)
#
# p2 = Person()
# p2.method = "POST"
# p2.payload = "太NB了"
# info = p2.SerializeToString()
# print(info)
#
# # 根据字节转换对象，由于业务处理(反序列化)
# obj = Message()
# obj.ParseFromString(info)
# print(obj.method)
# print(obj.payload)
#
# # 根据字节转换对象，用于业务处理(反序列化)
# obj = Message()
# print(dir(obj))

# 序列化
# b'\n\x07wupeiqi\x10\x13'
from v1_pb2 import Person, Message
p1 = Person()
p1.name = "wupeiqi"
p1.age = 19
info = p1.SerializeToString()
print(info)

# p2 = Message()
# p2.method = "POST"
# p2.payload = "太NB了"
# info = p2.SerializeToString()
# print(info)

# 了解原来结构，反序列化
# name: "wupeiqi"
# age: 19
obj = Person()
obj.ParseFromString(info)
print(obj.name)
print(obj.age)
