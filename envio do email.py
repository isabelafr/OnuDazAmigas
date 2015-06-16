
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:17:13 2015

@author: Bruna
"""


import smtplib
import turtle
import email
import poplib
from firebase import firebase
import time

FIREBASE_URL = "https://onudazamigas.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL, None)

if __name__ == '__main__':
    infos = fb.get('/', "Bruna")
    amigas = infos["Amigas"]
    email_amigas = amigas.values()
    print (len (email_amigas))
    problemas = infos["Problemas"]
    email_problemas = problemas.values()

#FROMADDR = "bruh.mdb@gmail.com"
#NOME = "Bruna Di Bisceglie"
#LOGIN    = "bruh.mdb@gmail.com"
#PASSWORD = "cisvv08ym11"
#TOADDRS  = "danielaamb@terra.com.br"
#SUBJECT  = "Test"
#ListaProblema = email_amigas
#ListaAmigas = email_problemas
#ONUADDR = "onudazamigas@gmail.com"
#ONUPASS = "onudazamigasbdfi"
#FROMONU = "ONU Dazamigas"
#
#janela = turtle.Screen()
#txt = janela.textinput("Mandar e-mail", "Digite o texto da sua mensagem")
#
##msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
##      # % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
#
#if TOADDRS in ListaProblema:
#    pergunta = txt + "\n\n  " + NOME + " quer mandar essa mensagem para: " + TOADDRS + "\n Voce autoriza o envio? (Responder apenas com: Sim/Nao)" 
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.set_debuglevel(1)
#    server.ehlo()
#    server.starttls()
#    server.login(ONUADDR, ONUPASS)
#    server.sendmail(FROMONU, ListaAmigas, pergunta)
#    server.quit()
##Se não estiver na lista problema
#else:    
##Mandar email
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.set_debuglevel(1)
#    server.ehlo()
#    server.starttls()
#    server.login(LOGIN, PASSWORD)
#    server.sendmail(FROMADDR, TOADDRS, txt)
#    server.quit()
#inicio = time.time()
#fim = 0
#sims = 0
#while fim - inicio < 1800:
#
#    mensagem2 = 0
#    user = ONUADDR
#    Mailbox = poplib.POP3_SSL('pop.googlemail.com', '995') 
#    Mailbox.user(user) 
#    Mailbox.pass_(ONUPASS) 
#    numMessages = len(Mailbox.list()[1])
#    for i in range(numMessages):
#        for msg in Mailbox.retr(i+1)[1]:
#            mensagem = str(email.message_from_bytes(msg))
#            if "sim" in mensagem:
#                sims += 1
#            if "nao" in mensagem:
#                mensagem2 = 2 
#    fim = time.time()
#    if mensagem2 == 2:
#        texto = "email nao enviado"
#        server = smtplib.SMTP('smtp.gmail.com', 587)
#        server.set_debuglevel(1)
#        server.ehlo()
#        server.starttls()
#        server.login(ONUADDR, ONUPASS)
#        server.sendmail(ONUADDR, FROMADDR, texto)
#        server.quit()
#        mandou = "recusado" 
#        break
#    if sims == 5:
#        #Mandar email
#        server = smtplib.SMTP('smtp.gmail.com', 587)
#        server.set_debuglevel(1)
#        server.ehlo()
#        server.starttls()
#        server.login(LOGIN, PASSWORD)
#        server.sendmail(FROMADDR, TOADDRS, txt)
#        server.quit()
#        mandou = "yes"
#    Mailbox.quit()
#if mandou != "yes" or mandou != "recusado":
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.set_debuglevel(1)
#    server.ehlo()
#    server.starttls()
#    server.login(LOGIN, PASSWORD)
#    server.sendmail(FROMADDR, TOADDRS, txt)
#    server.quit()