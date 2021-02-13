#!/usr/bin/env python3
import sys
from operator import itemgetter

current_word = None
current_count = 0

word = None
level = []
levelCount = []
source = []
sourceCount = []
date = []
dateCount = []
errorCount = []
key = []
value = []


for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    

    if current_word == word:
        current_count += count
    else:
        
        if current_count != 0:
            if (current_word.find("INFO")!=-1 or current_word.find("WARN")!=-1 or current_word.find("ERROR")!=-1) and current_word.find(": ")==-1:
                level.append(current_word)
                levelCount.append(current_count)
                
            if current_word.find("-") != -1:
                date.append(current_word)
                dateCount.append(current_count)
            
            if current_word.find(".") != -1:
                if current_word.find(": ERROR") != -1:
                    errorCount[-1] = current_count
                else:
                    source.append(current_word)
                    sourceCount.append(current_count)
                    errorCount.append(0)
        current_count = count
        current_word = word
        
        
    


if word == current_word :
    if (word.find("INFO")!=-1 or word.find("WARN")!=-1 or word.find("ERROR")!=-1) and word.find(": ")==-1:
        level.append(current_word)
        levelCount.append(current_count)

    if word.find("-") != -1:
        date.append(current_word)
        dateCount.append(current_count)

    if word.find(".") != -1:
        if word.find(": ERROR") != -1:
            errorCount[-1] = current_count
        else:
            source.append(current_word)
            sourceCount.append(current_count)
            errorCount.append(0)

levelLangeth = len(level)
sourceLangeth = len(source)
dateLangeth = len(date)
levelCountLangeth = len(levelCount)
sourceCountLangeth = len(sourceCount)
dateCountLangeth = len(dateCount)
errorCountLangeth = len(errorCount)


print("\n#1 How many logs are there in each log level")
count = 0
while True:
    print('%s\t%s'%(level[count],levelCount[count]))
    count += 1
    if count >= levelLangeth:
        break

print("\n#2 How many logs are there in each type of source")
count = 0
while True:
    print('%s\t%s'%(source[count],sourceCount[count]))
    count += 1
    if count >= sourceLangeth:
        break

print("\n#3 Which day has highest number of logs occurred and how many")
maxLog = max(dateCount)
index = dateCount.index(maxLog)
count = 0
print('%s\t%s'%(date[index],dateCount[index]))
maxError = max(errorCount)
index = errorCount.index(maxError)
print("\n#4 Which source has highest number of ERROR level logs occurred")
print('%s\t%s'%(source[index],errorCount[index]))

