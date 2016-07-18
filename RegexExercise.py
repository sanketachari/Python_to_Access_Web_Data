import re

hand = open('regex_sum_286827.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers)==0 : continue
    for number in numbers:
        num = int(number)
        numlist.append(num)
print sum(numlist)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('[0-9]+', x)
print y

