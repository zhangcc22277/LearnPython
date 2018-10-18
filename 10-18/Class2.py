#coding =utf-8
#面向对象中的lei

class Student(object):
    def __init__(self,name,score):
        self.name =name
        self.score=score
    def get_gender(self):
        if self.score>=90:
            return "A"
        elif self.score>=60:
            return 'B'
        else:
            return "C"
lisa =Student('Lisa',99)
bart = Student('Bart',59)
print (lisa.name,lisa.get_gender())
print (bart.name,bart.get_gender())
