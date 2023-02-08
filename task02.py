text = input().lower().split()    #Ищем сколько одинаковых слов в тексте
result = set()
for i in text:
    result.add(i)
print(len(result))    
