name=input("enter your name")
age=input("enter your age")
f=open("user_detaile.txt","a")
f.write(name)
f.write(age)
f.close()
