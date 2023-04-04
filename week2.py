w = "What"
i = "IS"
c = "CamelCase?"
print("{} {} {}" .format(w, i.lower(), c))

asx_value = 7111.4
date = '2021-01-25'
units = 1
currency = 'AUD'
print(f'The closing value of {units} unit of the All Ordinaries on {date} was {asx_value} {currency}.')





dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
print(dic0)
print(dic0['a'])

dic = { ['a', 'b']: 1, 'c': 2,}
dic = { ('a', 'b'): 1, 'c': 2, }

tup = (1, 2, ('a', 'b'))
dic = {tup: 'value'}

a=21312
b=2
c=3

print(f'a represents number {a}, b represents number {b},'
      f' c represents number {3}')
print('a represents number {}, b represents number {}, c represents number {}.'.format(a,b,c))


def f(a,b):
    value=a+b
    return value
print(f(1,2))

a='hello'
b=1
c=[1,2,3]
print(type(a))
print(type(b))
print(type(c))

a='I hAvE TwO ApPleS.'
print(a.lower())
a=a.lower()
print(a)


a='       I hAvE TwO ApPleS.      '
a=a.strip()
print(a)
a=a.capitalize()
print(a)
a=a.strip().lower().capitalize()
print(a)

txt=',,,asdaw...apple..sdr'
x=txt.strip()
print(x)
x=txt.strip(',..sdr') #从左边右边一起删，删到没有在括号里的为止
print(x)

#index 索引，用[]来进行操作
a='how are you?'
print(len(a)) # a的长度
print(a[0])
print(a[11])
# Slicing
print(a[0:5])
print(a[-12:-7]) #用0-12和5-12，因为一共有12个字符
print(a[2:])
print(a[:])
# print(list_1[::] #start:end:interval 最后一项如果输入负数，从后往前排序并且有间隔
list_1=[1,2,3]
list_1[0]=100  #把数列中第一个值改为100
print(list_1)

list_2=[1,2,3]
list_2.append(4)
print(list_2)
list_3=[1,2,3]
list_3.insert(1,10)  #把10插入在第二位
print(list_3)
list_3.insert(0,10) #把10插入在第一位
print(list_3)

list_4=[200,5,3,7,2]
list_4.sort()
print(list_4)
list_4.sort(reverse=True)
print(list_4)

# Method 2
list_4=sorted(list_4)
print(list_4)

# delete the last element
list_5=[1,2,3]
# list_5.pop()
# print(list_5)
list_5.pop(1)
print(list_5)

# Tuple 元组 不能修改 ordered
t=(1,2,3,4)
# tuple unpacking 重点
a,b=1,2
print(a,b)
a,b=(1,2)

# Dictionary
marks={'Ben':96, 'David':98, 'Cat':97}
print(marks)
# 增加元素
marks['Peter']=95
print(marks)