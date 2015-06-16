# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 09:59:24 2015

@author: Bruna
"""

from firebase import firebase

# Troque esta URL pela de seu próprio App Firebase
FIREBASE_URL = "https://onudazamigas.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL, None)


class Amigas(object):
	def nome(self,nome):
		self.nome = nome
	def email(self,email):
		self.email = email

class Problemas(object):
	def nome(self,nome):
		self.nome = nome
	def email(self,email):
		self.email = email



exit = False
i = 0
Amiga = []
Problema = []

nome = input("Escreva seu nome de usuario \n")
senha = input("Escreva sua senha \n")
Usuario = [0]*3
Usuario[0] = [{nome:senha}]
Usuario[1] = "Amigas"
Usuario[2] = "Problemas"
while exit == False:
	Amiga.append(Amigas())
	Amiga[i].nome = input("Escreva o nome da Amiga %d\n" %(i+1))
	Amiga[i].email = input("Escreva o email da %s\n"%Amiga[i].nome)
	sair = input("Você quer adicionar mais alguma amiga? (s/n)\n")
	i +=1
	if sair == "n":
		exit = True
	elif sair != "s":
		while sair != "s" and sair != "n":
			print("Erro, código não reconhecido.\n")
			sair = input("Você quer adicionar mais alguma amiga? (s/n)\n")
exit = False
i = 0
while exit == False:
	Problema.append(Problemas())
	Problema[i].nome = input("Escreva o nome do Problema %d\n" %(i+1))
	Problema[i].email = input("Escreva o email do  %s\n"%Problema[i].nome)
	sair = input("Você quer adicionar mais algum problema? (s/n)\n")
	if sair == "n":
		exit = True
	elif sair != "s":
		while sair != "s" and sair != "n":
			print("Erro, código não reconhecido.\n")
			sair = input("Você quer adicionar mais algum problema? (s/n)\n")
	i +=1


lista_email_problemas = []
lista_nomes_problemas = []

lista_email_amigas = []
lista_nomes_amigas = []

for treta in Problema:
	lista_email_problemas.append(treta.email)
	lista_nomes_problemas.append(treta.nome)
for treta in Amiga:
	lista_email_amigas.append(treta.email)
	lista_nomes_amigas.append(treta.nome)

dicAmigas = dict(zip(lista_nomes_amigas,lista_email_amigas))
dicProblemas = dict(zip(lista_nomes_problemas,lista_email_problemas))
lista = [dicAmigas, dicProblemas]
usu = dict(zip(Usuario[1:], lista))
usu[nome] = senha
if __name__ == '__main__':
    fb.put('/', nome, usu)