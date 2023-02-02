import os
import re

from git import *

repo = Repo("")
path = "."

# r=root, d=directories, f = files

total_map = {}



for r, d, f in os.walk(path):
    if(r.find(".git") > 0):
        continue
    for file in f:
        filepath = os.path.join(r, file)

        line_per_commit = []
        
        if(file == "main.py"):
            continue

        for commit, lines in repo.blame("HEAD", filepath):            
            for line in lines:
                line_per_commit.append((line, commit))

        nested_if_def_component = []

        for i in range(len(line_per_commit)):
            line = line_per_commit[i][0]
            commit = line_per_commit[i][1]

            splitted_line = line.split(" ")

            if(splitted_line[0] == "#ifdef"):              
                nested_if_def_component.append(splitted_line[1]) 

            if(splitted_line[0] == "#endif"):
                nested_if_def_component.pop()

            if(len(nested_if_def_component) == 0):
                continue

            joined_line_components = ".".join(nested_if_def_component)

            if joined_line_components not in total_map:
                total_map[joined_line_components] = {}
            
            if commit.author.name not in total_map[joined_line_components]:
                total_map[joined_line_components][commit.author.name] = 0
            

            total_map[joined_line_components][commit.author.name] = total_map[joined_line_components][commit.author.name] + 1
            
            print(total_map)
            #print(str(i) + " " + str(line_per_commit[i]))

        

print(total_map)