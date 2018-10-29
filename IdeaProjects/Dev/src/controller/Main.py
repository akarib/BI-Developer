#coding:utf-8

"""

Types strandards : (int)
                   (float)
                   (str)
                   (boolean)

"""


age  =  14
age2 = "25"

prix =250.20

name = False

print(type(name))


texte = "age is {} and price is :{}"
print ("my age is :", age)


print(texte.format(age, prix))

print("age is {} and price is :{}".format(age, prix))

user = input("user-name is : ")

password = input("password is : ")

if user == password or user in password:
     print("please choose another user or password")

else:
     print("the details are :", user, password)



