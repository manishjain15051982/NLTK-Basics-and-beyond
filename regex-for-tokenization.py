import re


text = 'A Linux server, like any other computer you may be familiar with, runs applications. To the computer, these are' \
       ' considered "processes" While Linux will handle the low-level, behind-the-scenes management in a process\'s ' \
       'life-cycle, you will need a way of interacting with the operating system to manage it from a higher-level.'

#print(re.split(' ', text))
#print(re.split('\s+', text))

#print(re.split('\W', text))

print(re.findall('\w+|\S|\w*', text))

#print(re.findall("\w+[-']+\w+", text))


# further issues with tokenization

