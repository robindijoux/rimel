import os 
import sys 
import time
import re


def contributerMatcher(date):
    regex = "(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])"
    dateRegex = re.compile(regex)
    if dateRegex.match(date):
        return True
    else:
        return False 


def read_file():
    contributors = []
 
    try:
        with open('test.txt', 'r') as f:
            for line in f:
                x =  line.split()
                name = x[1]
                if contributerMatcher(x[2]):
                   contributors.append(name[1:])
                else:
                    contributors.append(name[1:] + " " + x[2])

            print(contributors)    
    except Exception as e:
        print(e)


    
        


read_file()

