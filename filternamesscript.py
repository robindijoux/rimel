
import re
import shlex
import subprocess
import os
from git import *
import time


class Contributor:
    def __init__(self, my_bool, my_number):
        self.my_bool = my_bool
        self.my_number = my_number
    
    def set_bool(self, my_bool):
        self.my_bool = my_bool
        
    def set_number(self, my_number):
        self.my_number = my_number
        
    def get_bool(self):
        return self.my_bool
        
    def get_number(self):
        return self.my_number

    def __str__(self):
        return "boolean_value: {}, number_value: {}".format(self.my_bool, self.my_number)



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


def extractMainContributor(cmd ,  contributors , directory , file):
    contribs = []
    allcontribs = []
    os.popen(cmd)
    subprocess.run(["retrieve.sh"] , shell=True)
    time.sleep(3)
    try:
        with open('test1.txt', 'r') as f:
            for line in f:
              match = re.search(r'(\d+)\)\s+#(.*)', line)
              if match:
                    line_number = match.group(1)
                    preprocessor = match.group(2)
                    if re.match(r"ifdef", preprocessor):
                       contributor = Contributor(True , line_number)
                       contribs.append(contributor)
                    else:
                       contributor = Contributor(False , line_number)
                       contribs.append(contributor)
            for cont in contribs:
                print(cont)
            for i in range(0 , len(contribs) - 2):
                if(contribs[i].get_bool() == True and contribs[i + 1].get_bool() == False ):
                    print(contribs[i].get_bool())
                    print(contribs[i + 1].get_bool())
                    cmd1 = 'cd ' + directory[:-1] +  ' &git blame -L' + contribs[i].get_number() + ',' + contribs[i + 1].get_number() + " " + file +   ' > C:/Users/user/Documents/GitHub/rimel/ifdef.txt'
                    print(cmd1)
                    os.popen(cmd1)
                    print(os.getcwd())
                    allcontribs = extractAllContributors()
                    dict = set()
                    for name in allcontribs:
                        print(name)
                        dict.add((name,occurence(allcontribs,name)))
                    x = sorted(list(dict),key=lambda x: -x[1])  
                    contributors.append(x[0][0])
                else: 
                    continue
            for name in contributors:
                print("printing final names")
                print(name)    
            return contribs
    except Exception as e:
        print(e)



def extractAllContributors():
    contributors = []
    try:
        with open('bloccontribs.txt', 'r') as f:
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
            time.sleep(3)
            os.popen(cmd)
            time.sleep(2) 
            extractMainContributor(cmd ,  contributors , dirAndFile[0] , dirAndFile[1])
        else:
            continue    
   findPaternityOwner(contributors)


    
    
extractCommitsInfo()
#extractMainContributor()

#splitDirectoryFromFile()

#print(createCommand("busybox/archival/" , "gzip.c"))

#extractAllContributors([])



#print(fileMatcher("etworking/interface.c"))

#extractIfDefFiles()

#print(isFile("fahd") == True and isPackExtension("fahd.c") == False)

#print(splitDirectoryFromFile())






  


