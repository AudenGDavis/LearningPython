'''
Created on Nov 4, 2021

@author: adavis25
'''
import random
firstName = input("enter your first name: ")
lastName = input("enter your last name: ")

print (f"your full name is {firstName} {lastName} and your initials are {firstName[0]}.{lastName[0]}.")
print (f"your first name has {len(firstName)} characters and your last name has {len(lastName)} characters")

def merge (list):
    final = ''
    for x in range(0, len(list)):
        final = final + list[x]
    return final


def makeGram (myString):
    string_list = []
    for x in range(0, len(myString)):
        string_list.append(myString[x])
    final_list = []
    for x in range(0, len(string_list)):
        randomNum = random.randint(0, len(string_list)-1)
        final_list.append(string_list[randomNum])
        string_list.pop(randomNum)
    return final_list



print (f"""'{firstName}' scrambled is '{merge(makeGram(firstName))}' and '{lastName}' scrambled is '{merge(makeGram(lastName))}'""")
