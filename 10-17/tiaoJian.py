#coding =utf-8
#小明身高1.75，体重80.5  请根据BMI公式（体重处以身高的平方）帮小明计算他的BMI指数
#并根据BMI指数：
# 低于１８.５：过轻
# １８.５－２５：正常
# ２５－３２：肥胖
# 高于３２　：严重肥胖

height = 1.75
weight = 80.5

bmi = weight/(height*height)
print(bmi)
if bmi<18.5:
    print("过轻")
elif bmi<25:
    print("正常")
elif bmi<25:
    print("过重")
elif bmi <32:
    print("肥胖")
else:
    print("严重肥胖")