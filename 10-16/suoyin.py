#需求:要求输入年、月、日（1-12的数字）、日（1-31），然后打印出相应的日期的月份的名称等

#根据给定的年月日以数字的形式打印出日期
months=[
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December'
]
#以1-31的数字作为结尾的列表
ending=['st','nd','rd']+17*['th']\
	+['st','nd','rd']+17*['th']\
	+['st']

year= input('year:')
month =input('Month(1-12):')
day=input('Day(1-31:')

month_number = int(month)
day_number = int (day)

#记得将月份和天数减一，以获得正确的索引
month_name = months[month_number-1]
ordinal =day+ending[day_number-1]

print (month_name+''+ ordinal+ '.'+year)