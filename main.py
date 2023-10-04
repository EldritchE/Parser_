import re

# Paser 
returnFalse=[]
returnTrue=[]
with open('/home/tsom/parser/Parser_/results2030.txt','r') as plik:
    for line in plik :
        line=line.strip()
        if line.strip().endswith('se'):
            returnFalse.append(line)
            
        else:
            returnTrue.append(line) 
# print ("True")            
# for showTrue in  returnTrue:
#     print(showTrue)
# print('False')   
# for showFalse in  returnFalse:
#     print(showFalse)
    

with open('true.txt','w') as trueTxt:
    for element in returnTrue:
        trueTxt.write(element+'\n')
with open('false.txt','w') as falseTxt:
    for element in returnFalse:
        falseTxt.write(element+'\n')
        
#select uppon 2023 in False file
final=open ("final.txt",'w')
regularForDate = r'\d{2}\.\d{2}\.(\d{4})'
regularForDate = r'\d{2}\.\d{2}\.(\d{4})'
with open('false.txt','r') as file:
    for line in file:
        hit = re.search(regularForDate,line)
        if hit :
            year=int(hit.group(1))
            if year >= 2030:
                final.write(line)
final.close
print ("*************************")
with open('final.txt','r') as final:
    for line in final:
        print(line.strip())


for showFinal in  returnFalse:
    pass