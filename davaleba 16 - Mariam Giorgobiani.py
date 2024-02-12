#!/usr/bin/env python
# coding: utf-8

# In[17]:


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.balance}")   
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.balance}")
        
mariami = BankAccount("GE1234567898765362", "MARIAMI", 1000)
mariami.withdraw(100)

nino = BankAccount("GE132435467578969", "NINO", 4000)
nino.deposit(300)


# In[37]:


class Student:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = []
    
    def information(self, semester, year, total_credits):
        print(f"Student {self.name} with id_number {self.student_id} is on {year} year, {semester} semester and has {total_credits} credits")
    
    def register(self, courses):
        print(f"Student {self.name} with id_number {self.student_id} is registered on {self.courses}")
    
microeconomics_course = Course("micro1", "Microeconomics")
macroeconomics_course = Course("macro1", "Macroeconomics")
statistics_course = Course("stat1", "Statistics")
    
student_1 = Student("MARIAMI", 35001119182, microeconomics_course)
student_1.register()


# In[41]:


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
    
    def information(self, semester, year, total_credits):
        print(f"Student {self.name} with id_number {self.student_id} is on {year} year, {semester} semester and has {total_credits} credits")
    
    def register(self, course):
        self.courses.append(course)
        print(f"Student {self.name} with id_number {self.student_id} is registered for {course.course_name} course.")


microeconomics_course = Course("micro1", "Microeconomics")
macroeconomics_course = Course("macro1", "Macroeconomics")
statistics_course = Course("stat1", "Statistics")
    
student_1 = Student("Mariami", 35001119182)
student_1.register(microeconomics_course)

student_2 = Student("Nino", 35001119167)
student_2.register(statistics_course)


# In[ ]:




