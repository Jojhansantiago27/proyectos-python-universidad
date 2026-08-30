def triangulos(a,b,c):
  
    if a+b>c and a+c>b and b+c>a:
        return 1
    else:
        return 0
a=12
b=20
c=17

t=triangulos(a,b,c)
print(f"{t}")

