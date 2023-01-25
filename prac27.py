# class Company:
#     def __init__(self,company_name,name,designation,salary):
#         self.company_name=company_name
#         self.name=name
#         self.designation=designation
#         self.salary=salary
#
#     def show(self):
#         print(self.name)
#         print(self.designation)
#         print(self.salary)
#
# class smallcompany(Company):
#     def __init__(self,comany_name,name,designation,salary,location):
#         self.location=location
#         Company.__init__(self,comany_name,name,designation,salary)
#
#     def talk(self):
#         print("Company name:",self.company_name)
#         print("My name is:",self.name)
#         print("Designation is:",self.designation)
#         print("salary is:",self.salary)
#         print("work location is:",self.location)
#
# company1=smallcompany("mindtek","rehman","QA","11lpa","BANGLORE")
# company2=smallcompany("ust","vamsi","qa","13lpa","hyd")
# company1.show()
# print("--------------------")
# company1.talk()
# print("---------------------------------")
# company2.talk()
#
# class Hasanbaba:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#
#
#     def show(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#
# class humera(Hasanbaba):
#     def __init__(self,name,age,gender,dob):
#         self.dob=dob
#         Hasanbaba.__init__(self,name,age,gender)
#
#     def talk(self):
#         print("My name is {}".format(self.name))
#         print("Age is {}".format(self.age))
#         print("Gender is {}".format(self.gender))
#         print("dob is {}".format(self.dob))
#
# child1=humera("rehman",25,"male","07-08-1997")
# child2=humera("wajeed",5,"male","01-10-2018")
# child1.talk()
# print("-------------------")
# child2.talk()

#
# #
# n=int(input("enter number is::"))
# for i in range(2,n):
#         if n%i==0:
#             print(n,"not a prime")
#             break
# else:
#     print(n,"its a prime")

#
# input_number=int(input("entered input number is:"))
# for i in range(2,input_number):
#     if input_number % i==0:
#         print(input_number,"is not a prime")
#         break
# else:
#     print("prime",input_number)
#

#
# list1=[]
# for i in range(1,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
# else:
#     list1.append(i)
#

class parent:
    def pdisplay(self):
        print("parent")
    def display(self):
        print("welcome")


class parent1:
    def p1display(self):
        print("parent1")

    def display(self):
        print("good morning")

class child(parent,parent1):
    def cdisplay(self):
        print("child")

c1=child()

c1.display()






# class p1:
#     def __init__(self):
#         print("hi")
#
#     def __init__(self):
#         print("hello")
#
# c1=p1()




