#Python program to check whether a number is strong number or not
s=input("enter a no.")
n=0
for i in s:
    h=int(i)
    a=1
    for j in range(1,h+1):
        a*=j
    n+=a
if n==int(s):
    print("it is strong no.")
else:
    print("it is not a strong no.")
