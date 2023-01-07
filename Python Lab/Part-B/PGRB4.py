import re

def text_match(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return 'string matches as per requirment!'
    else:
        return('string not matching as per requerements')

def z_match(text):
    pattern = '\w*z.\w*'
    if re.search(pattern, text):
        return 'z found in the string'
    else:
        return('z Not found!')

def str_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')

print('1. find the sequences of one upper case letter followed by lower case letters')
print('2. match a word cont1aining letter z' )
print('3. match a string that contains only upper and lowercase letters, numbers,underscores') 
print('4. to remove leading zeros from an IP address')
c=int(input('enter your choice:'))
if (c==1):
    str= input('enter a string:')
    print(text_match(str))
elif(c==2):
    str= input('enter a string:')
    print(z_match(str))
elif(c==3):
    str= input('enter a string:')
    print(str_match(str)) 
elif(c==4):
    ip= input('enter ip address :')
    print('IP address after removing leading zeros')
    ip=re.sub('\.[0]*', '.', ip)
    print(ip.lstrip('0'))