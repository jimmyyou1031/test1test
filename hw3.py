print("Please type anything.")
elements = str(input())
dict={}
print(type(elements))
for a in elements:
    if a in dict:
        dict[a]+=1
    else:
        dict[a]=1
for t in dict:
    print(t,':',dict[t])
