
text = input().split()
result = {} 
for i in text:
    if i in result:
        print(f'{i}_{result[i]}',end = ' ')
    else:
        print(f'{i}_{0}',end = ' ')
result[i] = result.get(i,0) + 1
