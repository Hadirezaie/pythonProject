# tuple is a data structure like list but is immutable
tpl=(1,2,3,2,'Hello',2.5)
print(tpl)
print(tpl*2)
print(tpl.count(2))
print(tpl.index(2))

# converting list to tuple
lst=[1,2,3,2,5]
print(type(lst))
tpl1=tuple(lst)
print(type(tpl1))
print(tpl1)