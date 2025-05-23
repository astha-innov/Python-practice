# check for duplicates in list
some_list = ['a','b','c','d','e','d','c','a','b','a']
duplicates = []
for i in range(len(some_list)):
    for j in range(i+1,len(some_list)):
        if some_list[i]==some_list[j] and some_list[i] not in duplicates:
            duplicates.append(some_list[i])
print(duplicates)
    
