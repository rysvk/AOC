with open('input.txt', 'r') as file:
    data = file.read().strip()
cnt = 0
idx = 0 
for i in data:
    cnt+= 1 if i == '(' else -1 if i==')' else 0
    if(cnt == -1):
        print(idx+1)
        break
    idx+=1