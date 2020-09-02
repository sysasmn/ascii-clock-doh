

#!/usr/bin/python3

#testing printing numbers and removing with os.system("clear")
import time
import os
import digits

height = 16
width = 25

#create lines
global lines

def get_nth_line(digit, n):
    #put error checks here on digit or n

    newlines = 0; 
    output = ""
    for c in digits.numbers[digit]:
        if newlines < n-1:
            if c == "\n":
                newlines += 1;
                continue
        else:
            if c == "\n":
                return output
            output += c



def reach_width(line):
    dif = width - len(line)
    #print("len = ", len(line))
    if dif > 0:
        output = line + dif*" "
        return output
    return line


def nth_line_time(hour, minute, second, n):
    tens_hour = int(hour/10)
    units_hour = hour % 10

    tens_min = int(minute/10)
    units_min = minute % 10

    tens_second = int(second/10)
    units_second = second % 10

    return reach_width(get_nth_line(tens_hour,n)) + reach_width(get_nth_line(units_hour,n)) + reach_width(get_nth_line(tens_min,n)) + reach_width(get_nth_line(units_min,n)) + reach_width(get_nth_line(tens_second,n)) + reach_width(get_nth_line(units_second,n))


s = reach_width(get_nth_line(9,height))
print(s)
#time.sleep(5)
for i in range (1,height+1):
    print(nth_line_time(10,0,0,i))
#time.sleep(10)
while True:
    os.system("clear")

    t = time.time()
    Time = time.localtime(t)

    hour = Time.tm_hour
    second = Time.tm_sec
    minute = Time.tm_min

    for i in range (1,height+1):
        print(nth_line_time(hour,minute,second,i))    
    #print(hour)
    #print(minute)
    #print(second)

    time.sleep(0.5)

