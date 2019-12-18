import sys

current_word=None
current_count=0

for line in sys.stdin:
    line=line.strip()
    if current_word==line:
        current_count+=1
    else:
        if current_word:
            print("Count",current_word,"=",current_count)
        current_word=line
        current_count=1
if current_word==line:
    print("Count",current_word,"=",current_count)
        
    
