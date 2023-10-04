import re

# Paser 
returnFalse = []
returnTrue = []

with open('/home/tsom/parser/Parser_/results2030.txt', 'r') as plik:
    for line in plik:
        line = line.strip()
        if line.endswith('se'):
            returnFalse.append(line)
        else:
            returnTrue.append(line)

with open('true.txt', 'w') as trueTxt, open('false.txt', 'w') as falseTxt:
    for element in returnTrue:
        trueTxt.write(element + '\n')
    for element in returnFalse:
        falseTxt.write(element + '\n')

# 
regularForDate = r'\d{2}\.\d{2}\.(\d{4)}'
selected_lines = [line for line in open('false.txt', 'r') if re.search(regularForDate, line).group(1) >= '2030']

with open('final.txt', 'w') as final:
    final.writelines(selected_lines)

print("*************************")
with open('final.txt', 'r') as final:
    for line in final:
        print(line.strip())
