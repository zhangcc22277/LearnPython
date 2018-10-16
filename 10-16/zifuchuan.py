#coding =utf-8

#根据指定的宽度打印格式良好的价格列表

width= int(input("please enter width:"))

price_width =10
item_width = width-price_width

header_fmt ="{{:{}}}{{:>{}}}".format(item_width,price_width)
fmt        ="{{:{}}}{{:>{}.2f}}".format(item_width,price_width)
# 对齐 print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))
# 分别是左对齐、居中和右对齐，相当于{{:10}{:>35-10.f}}

print("="*width)

print(header_fmt.format("Item","price"))

print("-"*width)

print(fmt.format("Apples",0.4))
print(fmt.format("Pear",0.5))
print(fmt.format("Cantaloupes",1.92))
print(fmt.format("Dried Apricots(16 oz.)",8))
print(fmt.format("Prunes(4 lbs.)",12))

print("="*width)


