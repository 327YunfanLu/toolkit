lst1 = ['a']
print(f'This is lst1: {lst1}')

lst2 = ['b', lst1]
print(f'This is lst2: {lst2}')

lst2[1].append('c')
print(lst1)

# If statement
happy=True
if happy is True:
    print('I am happy')
print('This will print regardless of the value of happy')


1 == True
print(1 is True)

var1='a'
var2='a'
var3=['a']
var4=['a']

print(var1==var2)
print(var1 is var2)
print(var3==var4)
print(var3 is var4)

b= False
if b is True:
    print('b is True')
else:
    print('b is False')


a = -1
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")

happy=True
if happy is True:
    pass

name=input('Who are you?')
print('Welcome to the class', name)

hours_worked = int(input("Enter the number of hours worked this week:"))
hourly_rate = 51.45  # base hourly rate
overtime_rate = 88.9  # hourly rate for overtime hours
overtime_threshold = 35  # hours worked threshold for overtime

if hours_worked <= overtime_threshold:
    weekly_pay = hours_worked * hourly_rate
else:
    overtime_hours = hours_worked - overtime_threshold
    regular_hours = overtime_threshold
    weekly_pay = (regular_hours * hourly_rate) + (overtime_hours * overtime_rate)

print("Your weekly pay is: $", round(weekly_pay, 2))

letters_lst=['a','b','c','d']

for letter in letters_lst:
    print(letter)

numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

for a in range(1, 4):
    for b in range(1, 4):
        print(a, b)

for a in range(1, 4):
    for b in range(1, 4):
        if a<=b:
          print(a, b)

for even in range(0,10,2):
    print(even)
    if even>2:
        break
        print(even)

for even in range(0,10,2):
    print(even)
    if even>2:
        continue

for even in range(0,10,2):
    if even>2:
        continue
print(even)



x=4/2
y=2
z=2.0
print(x)
print(type(x))
print(type(y))
print(type(z))




my_list = [1, 2, 3, 4, 5, 6]
to_remove = [2, 4, 6]

for item in to_remove:
    if item in my_list:
        my_list.remove(item)

print(my_list)



print("Printing current and previous numbersum in a range (10)")
previous_num = 0
for i in range(1,11):
    sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum", sum)
    previous_num = i



list_a=['a','b','c','d','e']
for i in enumerate(list_a):
    print(i)

for x in enumerate(list_a, start=1):
    print(x)

for i,j in enumerate(list_a,start=1):
    print(i,j)

d={'one':1,'two':2,'three':3}
for i in d:
    print(i)

for i in d.values():
    print(i)

for i in d.keys():
    print(i)

for i in d.items():
    print(i)

for i in range(11):
    if i % 2 !=0:
        continue
    else:
        print(i)

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
times=['9am','12pm','3pm']

# #打印工作日的三个时间 (按顺序monday 9am monday12pm这样）
for day in days:
    if day == 'Saturday'or day=='Sunday':
        continue
    else:
        for time in times:
            print(f'day:{day}, time:{time}')


###找最大值, 利用loop的循环
a=[1,2,3,4,5,6,7,8,9]
max_point=a[0]
for i in a:
    if i>max_point:
        max_point=i

print(max_point)