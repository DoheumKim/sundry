### Author : Kim Doheum(김도흠)     GNU
### Date : 2022-11-23
# importing module
from time import sleep

#print(chr(97))     A
#print(chr(122))    Z

# variables
BACKSPACE = 32
A = 65      #chr(65) == 'A'
Z = 90
a = 97
z = 122
output = ''
intv = 0.0275      #time_interval(시간 간격) 단위: 초(second)
text = list(input('text? '))
alphabet = ''
index_text = 0
MAX_LEN = len(text)-1


##### Algorithm1 #####   Start with 'a' and Ending is 'z'
'''
alphabet = a
while True:
    if text[index_text] == chr(a):      #text가 a일때
        output += text[index_text]
        sleep(intv)
        
        if index_text < MAX_LEN:
            print(output,end='')
            print(text[index_text])
            index_text += 1
        else:
            print(output,end='')
            break
        
    if text[index_text] == chr(alphabet):       #alphabet변수(a~z까지 변함)가 입력한 text랑 일치할때 동작함
        output += text[index_text]
        sleep(intv)

        if index_text < MAX_LEN:
            print(output,end='')
            print(text[index_text])
            index_text += 1
            alphabet = a
        else:
            print(output,end='')
            break
        
    elif text[index_text] == chr(BACKSPACE):        #공백처리
        sleep(intv)
        output += ' '
        print(output)
        index_text += 1

    else:
        sleep(intv)
        print(output,end='')
        print(chr(alphabet))
        if alphabet < z:
            alphabet += 1

'''

##### Algorithm2 #####   Start with 'z' and Ending is 'a'
alphabet = z        # Changed
while True:
    if text[index_text] == chr(z):      #text가 z일때        # Changed
        output += text[index_text]
        sleep(intv)
        
        if index_text < MAX_LEN:
            print(output,end='')
            print(text[index_text])
            index_text += 1
        else:
            print(output,end='')
            break
        
    if text[index_text] == chr(alphabet):       #alphabet변수(a~z까지 변함)가 입력한 text랑 일치할때 동작함
        output += text[index_text]
        sleep(intv)

        if index_text < MAX_LEN:
            print(output,end='')
            print(text[index_text])
            index_text += 1
            alphabet = z        # Changed
        else:
            print(output,end='')
            break
        
    elif text[index_text] == chr(BACKSPACE):        #공백처리
        sleep(intv)
        output += ' '
        print(output)
        index_text += 1

    else:
        sleep(intv)
        print(output,end='')
        print(chr(alphabet))
        if alphabet > a:        # Changed
            alphabet -= 1        # Changed