#!/usr/bin/python3

#there is an issue with the top line of each number that should be fixed I think width needs to be standard
#also put colons in for the 00:00:00 format

import time
import os
import digits

height = 16
width = 26

def get_nth_line(digit, n):

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

while True:
    os.system("clear")

    t = time.time()
    Time = time.localtime(t)

    hour = Time.tm_hour
    second = Time.tm_sec
    minute = Time.tm_min

    for i in range (1,height+1):
        print(nth_line_time(hour,minute,second,i))    
    time.sleep(0.5)

