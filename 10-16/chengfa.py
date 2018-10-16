#乘法示例
#以正确的宽度在剧中的盒子中打印一个句子
#注意，整数除法运算符（//）只能在python2.2之后的版本使用

sentence = input("Sentence:")

screen_width = 80
text_width = len(sentence)
box_width = text_width+6
left_margin = (screen_width - box_width)//2

print("")
print(" "*left_margin+"+"+"-"*(box_width-2)+"+")
print(" "*left_margin+"|"+" "*text_width+"|")
print(" "*left_margin+"|"+     sentence+"|")
print(" "*left_margin+"|"+" "*text_width+"|")
print(" "*left_margin+"+"+"-"*(box_width-2)+"+")
print("")