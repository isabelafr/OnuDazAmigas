__author__ = 'Dani Bento'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from ProgramacaoBru import *
from firebase import firebase
import smtplib
import poplib
import time
import email

FIREBASE_URL = "https://onudazamigas.firebaseio.com/"
fb = firebase.FirebaseApplication(FIREBASE_URL, None)

usu_aux = fb.get('/', None)
usuariosfb = usu_aux.keys()

login = "default"
senha = "default"

usuario_menu = "default"
senha_menu = "default"

amiga1 = "default"
amiga2 = "default"
amiga3 = "default"
amiga4 = "default"
amiga5 = "default"
aemail1 = "default"
aemail2 = "default"
aemail3 = "default"
aemail4 = "default"
aemail5 = "default"

lista_nomes_amigas = [amiga1, amiga2, amiga3, amiga4, amiga5]
lista_email_amigas = [aemail1, aemail2, aemail3, aemail4, aemail5]
dicAmigas = dict(zip(lista_nomes_amigas, lista_email_amigas))

prob1 = "default"
prob2 = "default"
prob3 = "default"
prob4 = "default"
prob5 = "default"
pemail1 = "default"
pemail2 = "default"
pemail3 = "default"
pemail4 = "default"
pemail5 = "default"

lista_nomes_problemas = [prob1, prob2, prob3, prob4, prob5]
lista_email_problemas = [pemail1, pemail2, pemail3, pemail4, pemail5]
dicProblemas = dict(zip(lista_nomes_problemas, lista_email_problemas))

lista = [dicAmigas, dicProblemas]

emailpara = "default"
emailassunto = "default"
emailcont = "default"
usuario_menu = "default"

class Menu(Screen):
    pass
class NaoEntrou(Screen):
    pass
class CadastroAmigas(Screen):
    pass
class Cadastro(Screen):
    pass
class CadastroProblemas(Screen):
    pass
class Menu2(Screen):
    pass
class TelaEmail(Screen):
    pass

class MyScreenManager(ScreenManager):
    usuario_menu = "scr_default"
    senha_menu = "src_menu"
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.login = "default"
        self.usuario_menu = "default"
        self.senha_menu = "default"
        self.password = "default"
        self.password2 = "default"
        self.login_aux = "default"
    def confere_senha(self):
        global senha
        global login
        self.login = self.screens[1].ids["usuario"].text
        self.usuario_menu = self.screens[0].ids["usuario_menu"].text
        self.senha_menu = self.screens[0].ids["senha_menu"].text
        self.password = self.screens[1].ids["senha"].text
        self.password2 = self.screens[1].ids["senha2"].text
        if self.password == self.password2:
            login = self.login
            senha = self.password
            print("confere_senha ", login, senha)
            self.current = "CadastroAmigas"
        else:
            print("Senhas Diferentes")


    def usuarioexiste(self):
        global usuario_menu
        global senha_menu
        global usuariosfb
        self.usuario_menu = self.screens[0].ids["usuario_menu"].text
        self.senha_menu = self.screens[0].ids["senha_menu"].text
        usuario_menu = self.usuario_menu
        usuario_menu = usuario_menu.replace(".","&e&")
        senha_menu = self.senha_menu
        MyScreenManager.usuario_menu = self.usuario_menu
        MyScreenManager.senha_menu = self.senha_menu
        print(usuario_menu,senha_menu)
        if usuario_menu in usuariosfb:
            pasta = usu_aux[usuario_menu]
            senha = pasta[usuario_menu]
            if senha_menu == senha:
                print("yes")
                self.current = "Menu2"
            else:
                print("no")
                self.current = "NaoEntrou"
        else:
            print("no")
            self.current = "NaoEntrou"
        return usuario_menu,senha_menu
    def cadastraamigas(self):
        global amiga1
        global amiga2
        global amiga3
        global amiga4
        global amiga5
        global aemail1
        global aemail2
        global aemail3
        global aemail4
        global aemail5
        global lista_nomes_amigas
        global lista_email_amigas
        global dicAmigas
        self.amiga1 = self.screens[3].ids["amiga1"].text
        self.amiga2 = self.screens[3].ids["amiga2"].text
        self.amiga3 = self.screens[3].ids["amiga3"].text
        self.amiga4 = self.screens[3].ids["amiga4"].text
        self.amiga5 = self.screens[3].ids["amiga5"].text
        self.aemail1 = self.screens[3].ids["aemail1"].text
        self.aemail2 = self.screens[3].ids["aemail2"].text
        self.aemail3 = self.screens[3].ids["aemail3"].text
        self.aemail4 = self.screens[3].ids["aemail4"].text
        self.aemail5 = self.screens[3].ids["aemail5"].text
        amiga1 = self.amiga1
        amiga2 = self.amiga2
        amiga3 = self.amiga3
        amiga4 = self.amiga4
        amiga5 = self.amiga5
        aemail1 = self.aemail1
        aemail2 = self.aemail2
        aemail3 = self.aemail3
        aemail4 = self.aemail4
        aemail5 = self.aemail5
        lista_nomes_amigas = [amiga1,amiga2,amiga3,amiga4,amiga5]
        lista_email_amigas = [aemail1,aemail2,aemail3,aemail4,aemail5]
        dicAmigas = dict(zip(lista_nomes_amigas,lista_email_amigas))
       # lista_ordem = sorted(dicAmigas.values())
        if "" in dicAmigas:
            del dicAmigas[""]

        self.current = "CadastroProblemas"
        return dicAmigas

    def cadastraprobs(self):
        global prob1
        global prob2
        global prob3
        global prob4
        global prob5
        global pemail1
        global pemail2
        global pemail3
        global pemail4
        global pemail5
        global dicAmigas
        global dicProblemas
        global senha
        global login
        global fb
        self.prob1 = self.screens[4].ids["prob1"].text
        self.prob2 = self.screens[4].ids["prob2"].text
        self.prob3 = self.screens[4].ids["prob3"].text
        self.prob4 = self.screens[4].ids["prob4"].text
        self.prob5 = self.screens[4].ids["prob5"].text
        self.pemail1 = self.screens[4].ids["pemail1"].text
        self.pemail2 = self.screens[4].ids["pemail2"].text
        self.pemail3 = self.screens[4].ids["pemail3"].text
        self.pemail4 = self.screens[4].ids["pemail4"].text
        self.pemail5 = self.screens[4].ids["pemail5"].text
        prob1 = self.prob1
        prob2 = self.prob2
        prob3 = self.prob3
        prob4 = self.prob4
        prob5 = self.prob5
        pemail1 = self.pemail1
        pemail2 = self.pemail2
        pemail3 = self.pemail3
        pemail4 = self.pemail4
        pemail5 = self.pemail5
        lista_nomes_problemas = [prob1,prob2,prob3,prob4,prob5]
        lista_email_problemas = [pemail1,pemail2,pemail3,pemail4,pemail5]
        dicProblemas = dict(zip(lista_nomes_problemas,lista_email_problemas))
        if "" in dicProblemas:
            del dicProblemas[""]
        self.current = "Menu"
        Usuario = [0]*3
        login = login.replace(".","&e&")
        Usuario[0] = [{login:senha}]
        Usuario[1] = "Amigas"
        Usuario[2] = "Problemas"
        print(dicAmigas,dicProblemas)
        lista = [dicAmigas, dicProblemas]
        usu = dict(zip(Usuario[1:], lista))
        usu[login] = senha
        print(usu)
        fb.put('/', login, usu)
        return dicAmigas,dicProblemas
    def envioemail(self):
        global emailpara
        global emailassunto
        global emailcont
        global login
        inicio = time.time()
        fim = 0
        sims = 0
        self.emailpara = self.screens[6].ids["emailpara"].text
        self.emailassunto = self.screens[6].ids["emailassunto"].text
        self.emailcont = self.screens[6].ids["emailcont"].text
        self.login_aux = self.screens[0].ids["usuario_menu"].text
        login_aux = self.login_aux
        login_aux = login_aux.replace(".","&e&")
        emailpara = self.emailpara
        emailassunto = self.emailassunto
        emailcont = self.emailcont
        if __name__ == '__main__':
            infos = fb.get('/', login_aux)
            amigas = infos["Amigas"]
            email_amigas = amigas.values()
            num_amigas = len(email_amigas)
            problemas = infos["Problemas"]
            email_problemas = problemas.values()
            PASSWORD = infos[login_aux]
            login_aux = login_aux.replace("&e&",".")
            LOGIN = login_aux
            emailassunto  = "Test"
            ListaProblema = email_problemas
            ListaAmigas = email_amigas
            ONUADDR = "onudazamigas@gmail.com"
            ONUPASS = "onudazamigasbdfi"
            FROMONU = "ONU Dazamigas"
        if emailpara in ListaProblema:
            pergunta = emailcont + "\n\n  " + login_aux + " quer mandar essa mensagem para: " + emailpara + "\n Voce autoriza o envio? (Responder apenas com: Sim/Nao)"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.login(ONUADDR, ONUPASS)
            server.sendmail(FROMONU, ListaAmigas, pergunta)
            server.quit()
            mandou = "NO"
            mensagem = " "

            while fim - inicio < 300:

                mensagem2 = 0
                user = ONUADDR
                Mailbox = poplib.POP3_SSL('pop.googlemail.com', '995')
                Mailbox.user(user)
                Mailbox.pass_(ONUPASS)
                numMessages = len(Mailbox.list()[1])
                for i in range(numMessages):
                    print(sims)
                    i = 0
                    for msg in Mailbox.retr(i+1)[1]:
                        i+=1
                        print (i)
                        mensagem = str(email.message_from_bytes(msg))
                        print (mensagem)
                        if "sim" in mensagem.lower():
                            sims += 1
                        if "nao" in mensagem.lower():
                            mensagem2 = 2
                fim = time.time()
                if mensagem2 == 2:
                    texto = "email nao enviado"
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.set_debuglevel(1)
                    server.ehlo()
                    server.starttls()
                    server.login(ONUADDR, ONUPASS)
                    server.sendmail(ONUADDR, LOGIN, texto)
                    server.quit()
                    mandou = "yes"
                    break
                if sims == num_amigas:
                    #Mandar email
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.set_debuglevel(1)
                    server.ehlo()
                    server.starttls()
                    server.login(LOGIN, PASSWORD)
                    server.sendmail(LOGIN, emailpara, emailcont)
                    server.quit()
                    mandou = "yes"
                    break
                Mailbox.quit()

            if mandou != "yes":
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.set_debuglevel(1)
                server.ehlo()
                server.starttls()
                server.login(LOGIN, PASSWORD)
                server.sendmail(LOGIN, emailpara, emailcont)
                server.quit()

        #Se não estiver na lista problema
        else:
        #Mandar email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.login(LOGIN, PASSWORD)
            server.sendmail(LOGIN, emailpara, emailcont)
            server.quit()



root = Builder.load_string("""
MyScreenManager:
    Menu:
    Cadastro:
    NaoEntrou:
    CadastroAmigas:
    CadastroProblemas:
    Menu2:
    TelaEmail:

<Menu>:
    name: "Menu"
    canvas.before:
        Color:
            rgba: .2, 1, .3, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        Label:
            text: "Bem-vinda ao ONUDAZAMIGAS!"
            font_size: 50
            pos_hint: {"center_x":.5, "center_y":.9}
        GridLayout:
            size_hint_y: None
            size_hint_x: .65
            height: 80
            pos_hint: {"center_x":.5, "center_y":.6}
            cols:2
            Label:
                text: "Usuário (e-mail):"
                font_size: 20
            TextInput:
                id: usuario_menu
                font_size: 18
                multiline: False
                cursor_color: .2, 1, .3, 1
            Label:
                text: "Senha:"
                font_size: 20
            TextInput:
                id: senha_menu
                font_size: 18
                multiline: False
                password: True
                cursor_color: .2, 1, .3, 1
        Button:
            background_color: 1,1,1,.5
            text: "ENTRAR"
            font_size: 20
            font_color: 1, 1, 1, 1
            size_hint_y: .1
            size_hint_x: .2
            pos_hint: {"center_x":.5, "center_y":.35}
            on_release: root.manager.usuarioexiste()
        Button:
            background_color: 1,1,1,.5
            text: "CADASTRE-SE"
            font_size: 20
            size_hint_y: .1
            size_hint_x: .3
            pos_hint: {"center_x":.5, "center_y":.1}
            on_release: root.manager.current = "Cadastro"

<Cadastro>:
    name: "Cadastro"
    canvas.before:
        Color:
            rgba: .2, 1, .3, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        Label:
            text: "CADASTRE-SE"
            font_size: 50
            pos_hint: {"center_x":.5, "center_y":.9}
        GridLayout:
            size_hint_y: None
            size_hint_x: .8
            height: 140
            pos_hint: {"center_x":.5, "center_y":.5}
            cols:2
            Label:
                text: "Usuário (e-mail):"
                font_size: 20
            TextInput:
                id: usuario
                font_size: 18
                multiline: False
                cursor_color: .2, 1, .3, 1
            Label:
                text: "Senha:"
                font_size: 20
            TextInput:
                id:senha
                font_size: 18
                multiline: False
                password: True
                cursor_color: .2, 1, .3, 1
            Label:
                text: "Confirme sua senha:"
                font_size: 20
            TextInput:
                id: senha2
                font_size: 18
                multiline: False
                password: True
                cursor_color: .2, 1, .3, 1
        Button:
            background_color: 1,1,1,.5
            text: "CADASTRAR"
            font_size: 20
            size_hint_y: .1
            size_hint_x: .4
            pos_hint: {"center_x":.5, "center_y":.1}
            on_release: root.manager.confere_senha()

<NaoEntrou>:
    name: "NaoEntrou"
    canvas.before:
        Color:
            rgba: .2, 1, .3, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        Label:
            text: "SENHA INVÁLIDA OU"
            font_size: 60
            pos_hint: {"center_x":.5, "center_y":.8}
        Label:
            text: "USUÁRIO NÃO"
            font_size: 60
            pos_hint: {"center_x":.5, "center_y":.65}
        Label:
            text: "CADASTRADO!"
            font_size: 60
            pos_hint: {"center_x":.5, "center_y":.5}
        Button:
            background_color: 1,1,1,.5
            text: "VOLTAR"
            font_size: 20
            size_hint_y: .1
            size_hint_x: .2
            pos_hint: {"center_x":.5, "center_y":.2}
            on_release: root.manager.current = "Menu"

<CadastroAmigas>:
    name: "CadastroAmigas"
    canvas.before:
        Color:
            rgba: 1, 0, .4, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        Label:
            text: "Cadastre aqui suas amigas! (até 5)"
            font_size: 50
            pos_hint: {"center_x":.5, "center_y":.9}
        GridLayout:
            size_hint_y: None
            size_hint_x: .8
            height: 200
            pos_hint: {"center_x":.5, "center_y":.55}
            cols:2
            Label:
                text: "NOME"
                font_size: 25
            Label:
                text: "E-MAIL"
                font_size: 25
            TextInput:
                id: amiga1
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: aemail1
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: amiga2
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: aemail2
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: amiga3
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: aemail3
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: amiga4
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: aemail4
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: amiga5
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
            TextInput:
                id: aemail5
                font_size: 15
                multiline: False
                cursor_color: 1, 0, .4, 1
        Button:
            background_color: 1,1,1,.5
            text: "CADASTRAR"
            font_size: 20
            size_hint_y: .1
            size_hint_x: .3
            pos_hint: {"center_x":.5, "center_y":.2}
            on_release: root.manager.cadastraamigas()

<CadastroProblemas>:
    name: "CadastroProblemas"
    canvas.before:
        Color:
            rgba: 0, .5, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        Label:
            text: "Cadastre aqui as pessoas indesejadas! (até 5)"
            font_size: 38
            pos_hint: {"center_x":.5, "center_y":.9}
        GridLayout:
            size_hint_y: None
            size_hint_x: .8
            height: 200
            pos_hint: {"center_x":.5, "center_y":.55}
            cols:2
            Label:
                text: "NOME"
                font_size: 25
            Label:
                text: "E-MAIL"
                font_size: 25
            TextInput:
                id: prob1
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: pemail1
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: prob2
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: pemail2
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: prob3
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: pemail3
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: prob4
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: pemail4
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: prob5
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
            TextInput:
                id: pemail5
                font_size: 15
                multiline: False
                cursor_color: 0, .5, 1, 1
        Button:
            background_color: 1,1,1,.6
            text: "CADASTRAR"
            font_size: 20
            size_hint_y: .1
            size_hint_x: .3
            pos_hint: {"center_x":.5, "center_y":.2}
            on_release: root.manager.cadastraprobs()

<Menu2>:
    name: "Menu2"
    canvas.before:
        Color:
            rgba: .2, 1, .3, 1
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        Label:
            text: "O que você deseja fazer agora?"
            font_size: 48
            pos_hint: {"center_x":.5, "center_y":.9}
        Button:
            background_color: 1,1,1,.5
            text: "Mandar um e-mail!"
            font_size: 20
            size_hint_y: .3
            size_hint_x: .5
            pos_hint: {"center_x":.5, "center_y":.6}
            on_release: root.manager.current = "TelaEmail"
        Button:
            background_color: 1,1,1,.5
            text: "Sair"
            font_size: 20
            size_hint_y: .3
            size_hint_x: .4
            pos_hint: {"center_x":.5, "center_y":.2}
            on_release: root.manager.current = 0

<TelaEmail>:
    name: "TelaEmail"
    canvas.before:
        Color:
            rgba: .2, 1, .3, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "Escreva o e-mail que deseja enviar!"
        font_size: 45
        pos_hint: {"center_x":.5, "center_y":.9}
    GridLayout:
        size_hint_y: None
        size_hint_x: .3
        height: 200
        pos_hint: {"center_x":.2, "center_y":.6}
        cols:1
        Label:
            text: "Para:"
            font_size: 20
        Label:
            text: "Assunto:"
            font_size: 20
        Label:
            text: "E-mail:"
            font_size: 20
    GridLayout:
        size_hint_y: None
        size_hint_x: .6
        height: 100
        pos_hint: {"center_x":.65, "center_y":.65}
        cols:1
        TextInput:
            id: emailpara
            font_size: 18
            multiline: False
            cursor_color: .2, 1, .3, 1
        TextInput:
            id: emailassunto
            font_size: 18
            multiline: False
            cursor_color: .2, 1, .3, 1
    GridLayout:
        size_hint_y: None
        size_hint_x: .6
        height: 270
        pos_hint: {"center_x":.65, "center_y":.33}
        cols:1
        TextInput:
            id: emailcont
            font_size: 18
            multiline: True
            cursor_color: .2, 1, .3, 1
    Button:
        background_color: 1,1,1,.5
        text: "ENVIAR"
        font_size: 20
        size_hint_y: .1
        size_hint_x: .3
        pos_hint: {"center_x":.65, "center_y":.05}
        on_release: root.manager.envioemail()
        on_release: root.manager.current = "Menu2"

""")


class MainApp(App):
    def build(self):
        return root

if __name__=="__main__":
    MainApp().run()