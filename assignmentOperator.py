a=b=c=10;
print('result: ',a,b,c)

x,y=10,5;
x+=y;
print(x)
x*=y;
print(x)

# comparasion operator
x,y=77,55
print(x==y)

print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

# logical operator

x=20
y=30

print((x==20 and y==30))
print(x==21 and y==30)
print((x==10 or y==30))
print(not(x==10 or y==3))

# BMU
height=1.6
weight=50.0

bmi=weight/height**2
print(bmi)
if 21.0 < bmi < 33.0:
    print('normal')
elif bmi>33.0:
    print('Abnormal')
elif bmi<21.0 :
    print('Underweight')