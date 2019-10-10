#!/usr/bin/python
# coding: utf-8

# IMPORTS 
import unittest
import serviceimpl.accounts as ac

class testValidation(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(ac.funcAdd(2), 3, 'Add incorrect...')
    
    def testSub(self):
        self.assertEqual(ac.funcSub(2), 1, 'Sub incorrect...')
    
    def testMult(self):
        self.assertEqual(ac.funcMult(2), 4, 'Mult incorrect...')
    
    def testDiv(self):
        self.assertEqual(ac.funcDiv(4), 2, 'Div incorrect...')
    
    def testImc(self):
        self.assertEqual(ac.funcImc(90, 1.77), 'Sobrepeso', 'IMC incorrect...')
    
    def testOnlyUsersActivesInList(self):
        self.assertTrue(ac.funcValidateUsersActives(), 'Erro validation of users actives...')

    def testCountProfile(self):
        self.assertTrue(ac.funcValidateCountProfile(), 'Count profile incorrect...')
        
    def testCountSex(self):
        self.assertTrue(ac.funcValidateCountSex(), 'Count sex incorrect...')

    def testUserByMail(self):
        mail = 'joao.porto@dextra-sw.com'
        user = [ {'age': 28, 'id': 36, 'lastName': 'Porto', 'mail': 'joao.porto@dextra-sw.com', 'name': 'João Pedro', 'profile': 'MODERATOR', 'sex': 'M', 'status': 'PENDING'} ]
        self.assertEqual(ac.funcValidateUserByMail(mail), user, 'Erro in get user by mail...')

    def testUserById(self):
        userId = 3
        user = [ {  "id": 3,    "mail": "cccc@dextra-sw.com",         "name": "Laura",             "lastName": "Marques",    "sex": "F",   "status": "ACTIVE",     "profile": "STUDENT",        "age": 20  } ]
        self.assertEqual(ac.funcValidateUserById(userId), user, 'Erro in get user by id...')
    
    def testAverageOfAge(self):
        self.assertEqual(ac.funcValidateAverageOfAge(), 26.42, 'Erro validation of average of age...')
    
    def testRemoveCharacteresSpecials(self):
        value = 'João Pedro Porto'
        result = 'Joao Pedro Porto'
        self.assertEqual(ac.removeCharacteresSpecials(value), result, 'Erro in remove characteres specials...')
    
    def testNameLike(self):
        name = 'João Pedro'
        user = [ {  "id": 36,   "mail": "joao.porto@dextra-sw.com",   "name": "João Pedro",        "lastName": "Porto",      "sex": "M",   "status": "PENDING",     "profile": "MODERATOR",     "age": 28  } ]
        self.assertEqual(ac.funcQueryNameLike(name), user, 'Erro in find of user by like...')

    def testConcatNameAndLastNameOrderByAsc(self):
        names = [ 'Alice Oliveira', 'Arthur Marques', 'Bernardo Souza', 'Carlos Clemente', 'Cecília Oliveira', 'Davi Daólio', 'Eloá Oliveira', 'Enzo Oliveira', 'Gabriel Marques', 'Giovanna Oliveira', 'Guilherme Marques', 'Gustavo Souza', 'Heitor Daólio', 'Helena Oliveira', 'Heloísa Marques', 'Henrique Daólio', 'Isabella Souza', 'João Oliveira', 'João Pedro Porto', 'Júlia Marques', 'Laura Marques', 'Laura Marques', 'Lorena Oliveira', 'Lucas Marques', 'Luiza Marques', 'Lívia Oliveira', 'Manuela Marques', 'Maria Clara Marques', 'Maria Luiza Oliveira', 'Matheus Souza', 'Miguel Marques', 'Pedro Souza', 'Rafael Oliveira', 'Samuel Clemente', 'Sophia Souza', 'Valentina Marques' ]
        self.assertEqual(ac.funcValidateConcatNameAndLastNameOrderByName(), names, 'Erro concat name and last name and order by name...')

if __name__ == '__main__':
    unittest.main()