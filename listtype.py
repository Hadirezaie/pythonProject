from idlelib.replace import replace

lst=[1,2,"String",-5,5.2]
print(lst)
print(len(lst))
print(lst[3])
# print(lst.sort())

lst.append(40)
lst.remove("String")
del(lst[1])
print(lst)
lst.sort()
print(lst)

print(max(lst))
print(min(lst))
lst.insert(1,55)
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)