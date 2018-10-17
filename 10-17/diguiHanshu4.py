#coding =utf-8
#请编写move（n,a,b,c）函数，它接受参数n，他接受参数n，表示3个主子A、B、C、中第一个柱子的A盘子
#数量，然后打印出把所有盘子从A借助B移动到C的方法

def move(n,a,b,c):
    if n==1:
        print("move",a,"-->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(3,"A","B","C")
