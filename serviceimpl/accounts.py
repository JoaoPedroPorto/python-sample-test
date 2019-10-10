#!/usr/bin/python
# coding: utf-8

# IMPORTS
import json
import re

# READ FILE USER JSON
with open('./dao/user.json') as myFile:
    data = myFile.read()
users = json.loads(data)

def funcAdd(value):
    return value + 1

def funcSub(value):
    return value - 1

def funcMult(value):
    return value * 2

def funcDiv(value):
    return value / 2

def funcImc(weight, height):
    result = weight / pow(height, 2)
    result = round(result, 2)
    if result < 18.5:
        return 'Abaixo do peso'
    if result >= 18.5 and result <= 24.9:
        return 'Peso normal'
    if result >= 25 and result <= 29.9:	
        return 'Sobrepeso'
    if result >= 30 and result >= 34.9:
        return 'Obesidade grau 1'
    if result >= 35 and result <= 39.9:	
        return 'Obesidade grau 2'
    return 'Obesidade grau 3'

def funcValidateUsersActives():
    usersFiltered = funcQueryUsersActives()
    for user in usersFiltered:
        if user['status'] == 'INACTIVE':
            return False
    return True

def funcValidateCountProfile():
    profiles = funcQueryCountUsersByProfile()
    # GENERAL MANAGER 
    if profiles[0].get('count') != 9:
        return False
    # MODERATOR
    if profiles[1].get('count') != 9:
        return False
    # DRIVER 
    if profiles[2].get('count') != 9:
        return False
    # STUDENT
    if profiles[3].get('count') != 9:
        return False
    return True
    
def funcValidateCountSex():
    sexs = funcQueryCountUsersBySex()
    # MALE
    if sexs[0].get('count') != 18:
        return False
    # FEMALE
    elif sexs[1].get('count') != 18:
        return False
    return True

def funcValidateUserByMail(mail):
    return funcQueryGetUserByMail(mail)

def funcValidateUserById(id):
    return funcQueryGetUserById(id)

def funcValidateAverageOfAge():
    return funcQueryAverageOfAge()

def funcValidateNameLike(name):
    return funcQueryNameLike(name)

def funcValidateConcatNameAndLastNameOrderByName():
    return funcQueryConcatNameAndLastName()

#*** QUERYS ***#
# Query 01 - QUERY USERS ACTIVES
def funcQueryUsersActives():
    return list(filter(lambda user: (user['status'] != 'INACTIVE'), users))

# Query 02 - QUERY COUNT USERS BY PROFILE
def funcQueryCountUsersByProfile():
    countGenenalManager = 0
    countModerator = 0
    countDriver = 0
    countStudent = 0
    for user in users:
        if user['profile'] == 'GENERALMANAGER':
            countGenenalManager += 1
        elif user['profile'] == 'MODERATOR':
            countModerator += 1
        elif user['profile'] == 'DRIVER':
            countDriver += 1
        elif user['profile'] == 'STUDENT':
            countStudent += 1
    return [ 
                { 'profile': 'GENERALMANAGER', 'count': countGenenalManager }, 
                { 'profile': 'MODERATOR', 'count': countModerator }, 
                { 'profile': 'DRIVER', 'count': countDriver }, 
                { 'profile': 'STUDENT', 'count': countStudent } 
           ]

# Query 03 - QUERY COUNT USERS BY SEX
def funcQueryCountUsersBySex():
    countFemale = 0
    countMale = 0
    for user in users:
        if user['sex'] == 'M':
            countMale += 1
        elif user['sex'] == 'F':
            countFemale += 1
    return [ 
                { 'sex': 'M', 'count': countMale }, 
                { 'sex': 'F', 'count': countFemale } 
           ]

# Query 04 - QUERY GET USER BY MAIL
def funcQueryGetUserByMail(mail):
    return list(filter(lambda user: (user['mail'] == mail), funcQueryUsersActives()))

# Query 05 - QUERY GET USER BY ID
def funcQueryGetUserById(userId):
    return list(filter(lambda user: (user['id'] == userId), funcQueryUsersActives()))

# Query 06 - QUERY AVERAGE OF AGE
def funcQueryAverageOfAge():
    sumAge = 0
    for user in users:
        sumAge += user['age']
    average = sumAge / len(users)
    return round(average, 2)

# Query 07 - QUERY NAME LIKE JOAO
def funcQueryNameLike(name):
    funcQueryConcatNameAndLastName()
    name = removeCharacteresSpecials(name.upper())
    usersFiltered = []
    for user in users:
        if funcValidateLike(name, user['name']):
            usersFiltered = [ user ]
    return usersFiltered

# Query 08 - QUERY CONCAT NAME AND LAST NAME
def funcQueryConcatNameAndLastName():
    names = []
    for user in users:
        names.append(user['name'].strip() + " " + user['lastName'].strip())
    names.sort()
    return names

# AUXILIARY FUNCTIONS

def funcValidateLike(findName, currentName):
    currentName = removeCharacteresSpecials(currentName.upper())
    if findName in currentName:
        return True
    return False
    
def removeCharacteresSpecials(value):
    value.replace("ç","c")
    value.replace("Ç","C")
    value.replace("ñ","n")
    value.replace("Ñ","N")
    value = re.sub(r'[ãâàáä]', 'a', value)
    value = re.sub(r'[êèéë&]', 'e', value)
    value = re.sub(r'[îìíï]', 'i', value)
    value = re.sub(r'[õôòóö]', 'o', value)
    value = re.sub(r'[ûúùü]', 'u', value)
    value = re.sub(r'[ÃÂÀÁÄ]', 'A', value)
    value = re.sub(r'[ÊÈÉË]', 'E', value)
    value = re.sub(r'[ÎÌÍÏ]', 'I', value)
    value = re.sub(r'[ÕÔÒÓÖ]', 'O', value)
    value = re.sub(r'[ÛÙÚÜ]', 'U', value)
    return value