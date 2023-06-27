u = input("Is your number in mins or hrs?")
if u == "mins":
    i= int(input("What is your value?"))
    a= i/60
elif u =="hrs":
    i= int(input("What is your value?"))
    a = i*60
print(a)
