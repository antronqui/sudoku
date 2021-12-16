numero=int(input("dame un numero"))
total=0
for x in range(numero+1):
  if x==0:
      total=1
  else:
      total=total*x     
print (str(total))