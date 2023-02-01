
import re
import shlex
import subprocess
import os
from git import *
import time



def contributerMatcher(date):
    regex = "(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])"
    dateRegex = re.compile(regex)
    if dateRegex.match(date):
        return True
    else:
        return False

def fileMatcher(file):
    i = file.find(".")
    if (i < 0):
        return False
    else:
        return True
     


def extractAllContributors(contributors):
    try:
        with open('test.txt', 'r') as f:
            for line in f:
                x =  line.split()
                if fileMatcher(x[1]):
                   name = x[2]
                   if contributerMatcher(x[3]):
                        contributors.append(name[1:])
                   else:
                        contributors.append(name[1:] + " " + x[3]) 
                else:  
                    name = x[1]
                    if contributerMatcher(x[2]):
                        contributors.append(name[1:])
                    else:
                        contributors.append(name[1:] + " " + x[2]) 
            print(len(contributors))                         
            return contributors    
    except Exception as e:
        print(e)


def findPaternityOwner(contributors):
    dict = set()
    for name in contributors:
      dict.add((name,occurence(contributors,name)))
    determinePaternity(dict)

def occurence(liste, element):
    count = 0
    for i in liste:
        if i == element:
            count += 1
    return count


def determinePaternity(contributors): 
    x = sorted(list(contributors),key=lambda x: -x[1])
    print(x)


def extractIfDefFiles():
    
    dict = set()
    try:
         with open('ifdef_found.txt', 'r') as f:
          for line in f:
                x =  line.split(":")  
                dict.add(x[0])
         #print(dict)        
         return dict    
    except Exception as e:
        print(e)

def splitDirectoryFromFile():
    allFiles = extractIfDefFiles()
    result = []
    for dir in allFiles:
        x = dir.split("/") 
        dir = ""
        file = ""
        for i in range (len(x) - 1):         
           dir += x[i] + "/"
            
        file = x[len(x) - 1]
        result.append((dir , file))   
    return result

def createCommand(directory , file):
    cmd = 'cd ' + directory[:-1] +  ' &git blame ' + file +  ' > C:/Users/user/Documents/GitHub/rimel/ifdef.txt'
    return cmd

def isPackExtension(file):
     i = file.find(".pack")
     if i < 0:
        return False
     else:
        return True 
def isFile(file):
     i = file.find(".")
     if i < 0:
        return False
     else:
        return True           

def extractCommitsInfo(): 
   subprocess.run(["find-ifdef.sh", ""], shell= True)
   contributors = []
   splitedFilesAndDirs = splitDirectoryFromFile()
   print(os.getcwd())
#    cmd = 'cd tooltest/fahde & git blame one.c > C:/Users/user/Documents/GitHub/rimel/ifdef.txt'
#    os.popen(cmd) 
#    subprocess.run(["retrieve-info.sh"] , shell=True)
#    extractAllContributors(contributors)
   for dirAndFile in splitedFilesAndDirs:
        if(isFile(dirAndFile[1]) == True and isPackExtension(dirAndFile[1]) == False):
            cmd = createCommand(dirAndFile[0] , dirAndFile[1])
            print(cmd)
            print(dirAndFile[0] + "/" + dirAndFile[1])
            print("##########################################")
            os.popen(cmd)
            #time.sleep(2) 
            subprocess.run(["retrieve-info.sh"] , shell=True)
            extractAllContributors(contributors)
        else:
            continue    
   findPaternityOwner(contributors)


    
    
extractCommitsInfo()

#splitDirectoryFromFile()

#print(createCommand("busybox/archival/" , "gzip.c"))

#extractAllContributors()

#print(fileMatcher("etworking/interface.c"))

#extractIfDefFiles()

#print(isFile("fahd") == True and isPackExtension("fahd.c") == False)

#print(splitDirectoryFromFile())



 


