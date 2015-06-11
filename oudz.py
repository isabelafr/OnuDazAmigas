# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:54:30 2015

@author: Isabela
"""

import smtplib
import turtle
import email
import poplib
from firebase import firebase

def func1():
        texto = "A sua mensagem não foi enviada porque suas amigas não deixaram."
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(ONUADDR, ONUPASS)
        server.sendmail(FROMONU, FROMADDR, texto)
        server.quit()

def func2():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(LOGIN, PASSWORD)
        server.sendmail(FROMADDR, TOADDRS, txt)
        server.quit()
        
FIREBASE_URL = "https://onudazamigas.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL, None)

if __name__ == '__main__':
    email_amigas = fb.get('/', "Amigas")
    email_problemas = fb.get('/', "Problemas")
    amigas = email_amigas.values()
    problemas = email_problemas.values()

FROMADDR = "bruh.mdb@gmail.com"
NOME = "Bruna Di Bisceglie"
LOGIN    = "bruh.mdb@gmail.com"
PASSWORD = "cisvv08ym11"
TOADDRS  = "fefsgabriel@hotmail.com"
SUBJECT  = "Test"
ListaProblema = problemas
ListaAmigas = amigas
ONUADDR = "onudazamigas@gmail.com"
ONUPASS = "onudazamigasbdfi"
FROMONU = "ONU Dazamigas"

janela = turtle.Screen()
txt = janela.textinput("Mandar e-mail", "Digite o texto da sua mensagem")

#msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
#      # % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )

if TOADDRS in problemas:
    pergunta = txt + "\n\n A " + NOME + " quer mandar essa mensagem para: " + TOADDRS + "\n Voce autoriza o envio? (Responder apenas com: Sim/Nao)" 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(ONUADDR, ONUPASS)
    server.sendmail(FROMONU, ListaAmigas, pergunta)
    server.quit()
#Se não estiver na lista problema
else:    
#Mandar email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    server.sendmail(FROMADDR, TOADDRS, txt)
    server.quit()
    
while True:

    mensagem2 = 0
    user = ONUADDR
    Mailbox = poplib.POP3_SSL('pop.googlemail.com', '995') 
    Mailbox.user(user) 
    Mailbox.pass_(ONUPASS) 
    numMessages = len(Mailbox.list()[1])
    for i in range(numMessages):
        for msg in Mailbox.retr(i+1)[1]:
            mensagem = str(email.message_from_bytes(msg))
            if "sim" in mensagem:
                func1()
            if "nao" in mensagem:
                func2()
#    if mensagem2 == 2:
#        texto = "A sua mensagem não foi enviada porque suas amigas não deixaram."
#        server = smtplib.SMTP('smtp.gmail.com', 587)
#        server.set_debuglevel(1)
#        server.ehlo()
#        server.starttls()
#        server.login(ONUADDR, ONUPASS)
#        server.sendmail(FROMONU, FROMADDR, texto)
#        server.quit()
#    if mensagem2 == 1:
        #Mandar email
#        server = smtplib.SMTP('smtp.gmail.com', 587)
#        server.set_debuglevel(1)
#        server.ehlo()
#        server.starttls()
#        server.login(LOGIN, PASSWORD)
#        server.sendmail(FROMADDR, TOADDRS, txt)
#        server.quit()
    Mailbox.quit()