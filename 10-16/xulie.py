#序列成员

#检查用户名和PIN码
database = [
['albert','123'],
['dibert','4241'],
['smith','7524'],
['jones','9843']
]
username = input("User name:")
pin = intput("PIN code:")
if([username,pin] in database)
	print("granted")
