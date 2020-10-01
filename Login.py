from controler import CtrLogin
from tkinter import *


tst = CtrLogin()

class View_login():

    def start(self):
        return self.login_usu()

    def login_usu(self):
        self.janela = Tk()  # Cria a tela principal
        self.janela.resizable(0, 0)  # Impede que a telaseja redimensionada
        quadro = Frame(self.janela, bd=2, relief="raised", pady=80, padx=80)
        quadro.place(x=170, y=70)  # posiciona o quadro na posição
        fonte = ('Arial', '16', 'bold')

        self.usu = Entry(quadro, font=fonte, width=16)
        sps = Label(quadro)
        sps2 = Label(quadro)
        self.senha = Entry(quadro, font=fonte, width=16, show="*")
        bt1 = Button(quadro, font=fonte, text="Entrar", fg="black", activebackground="#A9A9A9", activeforeground="green", command=self.bt_onclick, width=12)


        self.usu.grid(row=0, column=2)
        sps.grid(row=1 , column=2)
        self.senha.grid(row=2, column=2)
        sps2.grid(row=3, column=2)
        bt1.grid(row=4, column=2, columnspan=2)

        self.janela.geometry("700x400+200+200")
        self.janela.title("Login")
        self.janela.mainloop()


    def bt_onclick (self, *usu, **senha):#função btn funcionando
        usuLog = self.usu.get()
        senhaLog = self.senha.get()
        tst.vali_logusu(usuLog, senhaLog)


if __name__ == "__main__":
    main = View_login()
    main.start()













