def qan_tic():
    tic='QAN.AX'
    print(tic)
    return tic
res=qan_tic()
print(res)

def qan_tic():
    tic='QAN.AX'
    print(tic)
    return tic
tic='WES.AX'
print(tic)

def qan_tic():
    print(tic)
    return tic
tic='WES.AX'
print(tic)
qan_tic()


def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
even_numbers = get_even_numbers(numbers)
print(even_numbers)

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
squares = [x**2 for x in lst if x**2 > 150]
print(squares)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
unique_evens = list(set([num for num in numbers if num % 2 == 0]))
print(unique_evens)

odd_list =[]
for i in range(1,31):
    if i %2 !=0:
        odd_list.append(i)
print(odd_list)

# comprehension
odd_lst = [i for i in range(1,31) if i%2 !=0]
print(odd_lst)


def p_func(a): #设定一个函数
    print(a) #指令是打印a
p_func(100) #调用函数p_funk

def func(a,b,c):
    return a+b+c
params = {'a':1, 'b':2, 'c':3} #调用字典函数
print(func(**params))

s="Hello World"
s=s.split(' ')
print(s)
s=[word.upper() for word in s]
print(s)


def upper_word(string):
    string=string.split()
    string=[word.upper() for word in string]
    return string
print(upper_word("I am Superman"))


long_sentence = 'I have a very interesting class tomorrow'
long_sentence = long_sentence.split(' ')
print(long_sentence)
### 如果我想要特定的奇数字符串在上述long_sentence里
words_selected= []
for numb,word in enumerate(long_sentence):
    if numb % 2 !=0:
        words_selected.append(word)

print(words_selected)

words_selected= [word for numb,word in enumerate(long_sentence) if numb %2 !=0]
print(words_selected)

def selected_words(string):
    string=string.split(" ")
    words=[word for num,word in enumerate(string) if num %2 !=0]
    return words

print(selected_words('I have a very interesting class tomorrow'))

s=0
for i in range(1,31):
    if i % 3 ==0:
        print(i)
        s=s+i
print(s)

def fun_sum(n):
    n = n + 1
    s= 0
    for i in range(n):
        if i % 3 ==0:
            s= s +i
    return s
print(fun_sum(30))