from tkinter import messagebox
from conect_bd import *


banco = ConectaBanco()

class CtrLogin():

    def vali_logusu(self, usuLog, senhaLog):
        usu_log = str(usuLog)
        pass_log = str(senhaLog)
        where = ("log_usu = '%s'" % usu_log)
        And = ("senha = '%s'" % pass_log)
        try:
            reg = banco.select("log_usu, senha", "log_caix", where, And)
            if reg:
                messagebox.showinfo("Sucesso", "Login efetuado com sucesso")
            if not reg:
                messagebox.showerror("Negado", "Verifique seu usuario e senha")
        except:
            messagebox.showerror("Problema no sistema", "entre em contato com os desenvolvedores!!")

    def salvar_pedi(self, Cpf, Nome, Ende, Num, Comp, Tel, Cel, Sbr, Vlr, Borda, Bebida, Total):
        print("test2")
        cpf = str(Cpf)
        nome = str(Nome)
        ende = str(Ende)
        num = str(Num)
        comp = str(Comp)
        tel = str(Tel)
        cel = str(Cel)
        sbr = str(Sbr)
        vlr = str(Vlr)
        borda = str(Borda)
        bebida = str(Bebida)
        total = str(Total)
        reg = 1
        campos = "cpf, nome, endereço, numero, complemento, tel, cel, sbr_pizz, valor,borda, bebida, total"
        valores = ("'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s'" % (cpf, nome, ende, num, comp, tel, cel,
                                                                               sbr, vlr, borda, bebida, total))
        try:
            banco.insert("pedi_cli", valores, campos)
        except:
            messagebox.showerror("Falha", "Não foi possivel cadastrar!")
        else:
            messagebox.showinfo("sucesso", "seu pedido foi salvo")

    def Delete_pedido(self, cpf):
        Cpf = str(cpf)
        where = ("cpf = '%s'" % Cpf)

        try:
            banco.delete("pedi_cli", where)
        except:
            messagebox.showerror("erro", "falha no sistema")
        else:
            messagebox.showinfo("sucesso", "pedi exluido")










