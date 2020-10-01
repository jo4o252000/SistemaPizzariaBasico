from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from controler import CtrLogin
from conect_bd import *



class View_home():

    def start1(self):
        return self.Home()

    def Home(self):
        janela = Tk()  # Cria a tela principal

        janela.resizable(0, 0)  # Impede que a telaseja redimensionada
        abas = Notebook(janela, width=490, height=350)
        fonte = ('Arial', '16', 'bold')

        frameHome = Frame(abas)
        frameAbaPedido = Frame(abas)
        frameAbaPedidoConsulta = Frame(abas)
        frameAbaCadastro = Frame(abas)

        abas.add(frameHome, text="Home")
        abas.add(frameAbaPedido, text="Pedido Cliente")
        abas.add(frameAbaPedidoConsulta, text="Consulta de pedidos")
        abas.pack(fill=BOTH, expand=1)
        #home
        img = PhotoImage(file="img/logo_pizza.png")
        label_imagem = Label(frameHome, image=img).pack()

        #pedido cliente
        btphoto= PhotoImage(file="img/lupa.png")
        bg = btphoto.subsample(30, 30)
        btnPhotoCon = PhotoImage(file="img/btnConfir.png")
        btnConfir = btnPhotoCon.subsample(3, 3)
        btnPhotoLimp = PhotoImage(file="img/btnCancel.png")
        btnCancelar = btnPhotoLimp.subsample(3, 3)
        lbCpf = Label(frameAbaPedido, text="cpf do cliente:", font=fonte)
        self.inpCpf = Entry(frameAbaPedido, font=fonte, width=15)
        lbNome = Label(frameAbaPedido, text="Nome cliente:", font=fonte)
        self.inpNome = Entry(frameAbaPedido, font=fonte, width=15)
        lbEnde = Label(frameAbaPedido, text="Endereço:", font=fonte)
        self.inpEnde = Entry(frameAbaPedido, font=fonte, width=25)
        lbNum = Label(frameAbaPedido, text="Numero:", font=fonte)
        self.inpNum = Entry(frameAbaPedido, font=fonte, width=15)
        lbComp = Label(frameAbaPedido, text="Complemento:", font=fonte)
        self.inpComp = Entry(frameAbaPedido, font=fonte, width=15)
        lbTel = Label(frameAbaPedido, text="Telefone:", font=fonte)
        self.inpTel = Entry(frameAbaPedido, font=fonte, width=20)
        lbCel = Label(frameAbaPedido, font=fonte, text="Celular:")
        self.inpCel = Entry(frameAbaPedido, font=fonte, width=15)
        lbPizzaLay = Label(frameAbaPedido, text=" ->Escolha sua Pizza", font=fonte)
        lbComboPizza = Label(frameAbaPedido, text="escolha o sabor da pizza:", font=fonte)
        self.inpSaborPizza = ttk.Combobox(frameAbaPedido, font=fonte, values=["Á Moda da Casa", "Alho e Óleo", "Aliche","Ao Funghi", "Atum","Baiana","Bauru","Caipira","Calabresa","Caponesa","Canadense","Capri","Catupiry","Cubana", "Escarola","Firense", "Frango","Gramute", "Gratinada","Grega","Imperial", "Margherita", "Matriciana","Mexicana","Moda da Casa", "Mussarela", " Napolitalho", "Napolitano","Oba Oba","Palmito", "Portuguesa", "Provolone","Quatro Queijos", "Romana", "Rústica","Seciliana", "Torino", "Toscana", "Veneza", "vienense"], width=15)
        btnBuscarPizza = Button(frameAbaPedido, image=bg, command = self.btn_buscPizz)
        lbValor = Label(frameAbaPedido, text="valor: R$", font=fonte)
        self.inpValor = Entry(frameAbaPedido, font=fonte, width=14)
        lbBorda = Label(frameAbaPedido, font=fonte, text="escolha a borda:")
        self.inpBorda = ttk.Combobox(frameAbaPedido, font=fonte, values=["Tradicional", "cheddar", "catupity","vulcão"], width=15)
        lbBebida = Label(frameAbaPedido, text="escolha a bebida:", font=fonte)
        self.inpBebida = ttk.Combobox(frameAbaPedido, font=fonte, values=["Nenhuma", "Pepsi", "Coca-cola", "Guarana", "Fanta", "Dolly"], width=15)
        btnConfirmar = Button(frameAbaPedido,image=btnConfir, command=self.btn_salvar)
        self.btnLimpar = Button(frameAbaPedido, image=btnCancelar, command=self.btn_limparTela)
        btnFinalizar = Button(frameAbaPedido,font=fonte,text="Finalizar Pedido", width=15, command=self.btn_Finalizr)
        lbTotal = Label(frameAbaPedido, font=fonte, text="Total:R$")
        self.inpTotal = Entry(frameAbaPedido, font=fonte, width=15)

        lbCpf.place(x=10, y=20)
        self.inpCpf.place(x=160, y=20)
        lbNome.place(x=350, y=20)
        self.inpNome.place(x=495, y=20)
        lbEnde.place(x=10, y=60)
        self.inpEnde.place(x=120, y=60)
        lbNum.place(x=450, y=60)
        self.inpNum.place(x=550, y=60)
        lbComp.place(x=758, y=60)
        self.inpComp.place(x=915, y=60)
        lbTel.place(x=10, y=100)
        self.inpTel.place(x=120, y=100)
        lbCel.place(x=390, y=100)
        self.inpCel.place(x=480, y=100)
        lbPizzaLay.place(x=5, y=150)
        lbComboPizza.place(x=10, y=200)
        self.inpSaborPizza.place(x=280, y=200)
        btnBuscarPizza.place(x=490, y=200)
        lbValor.place(x=550, y=200)
        self.inpValor.place(x=650, y=200)
        lbBorda.place(x=10, y=250)
        self.inpBorda.place(x=190, y=250)
        lbBebida.place(x=10, y=300)
        self.inpBebida.place(x=200, y=300)
        btnConfirmar.place(x=10, y=470)
        self.btnLimpar.place(x=140, y=470)
        btnFinalizar.place(x=10, y=350)
        lbTotal.place(x=10, y=400)
        self.inpTotal.place(x=100, y=400)

        #consulta pedido
        lbPedido = Label(frameAbaPedidoConsulta,text="Numero do pedido:", font=fonte)
        self.inpNumPedido = Entry(frameAbaPedidoConsulta, font=fonte, width=5)
        lbcpf = Label(frameAbaPedidoConsulta, text="cpf do cliente:", font=fonte)
        self.inpcpf = Entry(frameAbaPedidoConsulta, font=fonte, width=15)
        lbnome = Label(frameAbaPedidoConsulta, text="Nome cliente:", font=fonte)
        self.inpnome = Entry(frameAbaPedidoConsulta, font=fonte, width=15 )
        lbende = Label(frameAbaPedidoConsulta, text="Endereço:", font=fonte)
        self.inpende = Entry(frameAbaPedidoConsulta, font=fonte, width=25)
        lbnum = Label(frameAbaPedidoConsulta, text="Numero:", font=fonte)
        self.inpnum = Entry(frameAbaPedidoConsulta, font=fonte, width=15)
        lbcomp = Label(frameAbaPedidoConsulta, text="Complemento:", font=fonte)
        self.inpcomp = Entry(frameAbaPedidoConsulta, font=fonte, width=15)
        lbtel = Label(frameAbaPedidoConsulta, text="Telefone:", font=fonte)
        self.inptel = Entry(frameAbaPedidoConsulta, font=fonte, width=20)
        lbcomboPizza = Label(frameAbaPedidoConsulta, text="escolha do sabor da pizza:", font=fonte)
        self.inpsaborPizza = Entry(frameAbaPedidoConsulta, font=fonte, width=14)
        btnbuscarCli = Button(frameAbaPedidoConsulta, image=bg, command=self.btn_BCliente)
        lbvalor = Label(frameAbaPedidoConsulta, text="Total: R$", font=fonte)
        self.inpvalor = Entry(frameAbaPedidoConsulta, font=fonte, width=14)
        lbborda = Label(frameAbaPedidoConsulta, font=fonte, text="escolha da borda:")
        self.inpborda = Entry(frameAbaPedidoConsulta, font=fonte, width=14)
        lbbebida = Label(frameAbaPedidoConsulta, text="escolha da bebida:", font=fonte)
        self.inpbebida = Entry(frameAbaPedidoConsulta, font=fonte, width=14)
        self.btndelete = Button(frameAbaPedidoConsulta, image=btnCancelar, command=self.btn_DELpedi)


        lbPedido.place(x= 750, y=20)
        self.inpNumPedido.place(x=950, y=20)
        lbcpf.place(x=10, y=20)
        self.inpcpf.place(x=160, y=20)
        lbnome.place(x=400, y=20)
        self.inpnome.place(x=550, y=20)
        lbende.place(x=10, y=60)
        self.inpende.place(x=120, y=60)
        lbnum.place(x=450, y=60)
        self.inpnum.place(x=550, y=60)
        lbcomp.place(x=758, y=60)
        self.inpcomp.place(x=915, y=60)
        lbtel.place(x=10, y=110)
        self.inptel.place(x=120, y=110)
        lbcomboPizza.place(x=10, y=150)
        self.inpsaborPizza.place(x=300, y=150)
        btnbuscarCli.place(x=350, y=20)
        lbvalor.place(x=500, y=150)
        self.inpvalor.place(x=600, y=150)
        lbborda.place(x=10, y=200)
        self.inpborda.place(x=210, y=200)
        lbbebida.place(x=10, y=250)
        self.inpbebida.place(x=220, y=250)
        self.btndelete.place(x=10, y=310)


        janela.geometry("1120x590+400+100")
        janela.title("LAMIGLIORE PIZZA")
        janela.iconbitmap("img/BT_log.ico")
        janela.mainloop()

    def btn_Finalizr(self):
        valorPizza = self.inpValor.get()
        vlrPizza = float(valorPizza)
        bebida = self.inpBebida.get()
        if "Pepsi" == bebida:
            result = vlrPizza+4.5
            self.inpTotal.insert(0, result)
        if "Coca-cola" == bebida:
            result = vlrPizza+6.0
            self.inpTotal.insert(0, result)
        if "Guarana" == bebida:
            result = vlrPizza+5.5
            self.inpTotal.insert(0, result)
        if "Fanta" == bebida:
            result = vlrPizza+7.0
            self.inpTotal.insert(0, result)
        if "Dolly" == bebida:
            result =vlrPizza+3.5
            self.inpTotal.insert(0, result)
        if "Nenhuma" == bebida:
            self.inpTotal.insert(0, vlrPizza)

    def btn_salvar(self):

        Cpf = self.inpCpf.get()
        Nome = self.inpNome.get()
        Ende = self.inpEnde.get()
        Num = self.inpNum.get()
        Comp = self.inpComp.get()
        Tel = self.inpTel.get()
        Cel = self.inpCel.get()
        Sbr = self.inpSaborPizza.get()
        Vlr = self.inpValor.get()
        Borda = self.inpBorda.get()
        Bebida = self.inpBebida.get()
        Total = self.inpTotal.get()
        ctrl = CtrLogin()
        ctrl.salvar_pedi(Cpf, Nome, Ende, Num, Comp, Tel, Cel, Sbr, Vlr, Borda, Bebida, Total)

        self.inpCpf.delete(0, END)
        self.inpNome.delete(0, END)
        self.inpEnde.delete(0, END)
        self.inpNum.delete(0, END)
        self.inpComp.delete(0, END)
        self.inpTel.delete(0, END)
        self.inpCel.delete(0, END)
        self.inpSaborPizza.delete(0, END)
        self.inpValor.delete(0, END)
        self.inpBorda.delete(0, END)
        self.inpBebida.delete(0, END)
        self.inpTotal.delete(0, END)

    def btn_limparTela(self):

        self.inpCpf.delete(0, END)
        self.inpNome.delete(0, END)
        self.inpEnde.delete(0, END)
        self.inpNum.delete(0, END)
        self.inpComp.delete(0, END)
        self.inpTel.delete(0, END)
        self.inpCel.delete(0, END)
        self.inpSaborPizza.delete(0, END)
        self.inpValor.delete(0, END)
        self.inpBorda.delete(0, END)
        self.inpBebida.delete(0, END)
        self.inpTotal.delete(0, END)

        messagebox.showinfo("Limpeza", "Seu formulario de cadastro de pedido foi limpo !")

    def btn_buscPizz(self):
        sbr_pizz = self.inpSaborPizza.get()
        Cpizz = str(sbr_pizz)
        banco = ConectaBanco()
        where = ("sbr_pizza = '%s'" % Cpizz)
        try:
            reg = banco.select("*", "sbr_pizz", where)
            if not reg:
                messagebox.showerror("Sem resultado", "pizza não disponivel")
            else:
                messagebox.showinfo("sucesso", "pizza disponivel")
                for registro in reg:
                    self.inpValor.insert(0, registro[2])
        except:
            messagebox.showwarning("Problema", "problema no sistema consulte o desenvolvedor")

    def btn_BCliente(self):
        cpf = self.inpcpf.get()
        banco = ConectaBanco()
        where = ("cpf = '%s'" % cpf)

        try:
            reg = banco.select("*", "pedi_cli", where)
            if not reg:
                messagebox.showinfo("não foi encontrado", "pedido não foi encontrado")
            else:
                messagebox.showinfo("sucesso", "Pedido encontrado com sucesso ")
                for registro in reg:
                    print(registro)
                    self.inpNumPedido.insert(0, registro[0])
                    self.inpnome.insert(0, registro[2])
                    self.inpende.insert(0, registro[3])
                    self.inpnum.insert(0, registro[4])
                    self.inpcomp.insert(0, registro[5])
                    self.inptel.insert(0, registro[6])
                    self.inpsaborPizza.insert(0, registro[8])
                    self.inpvalor.insert(0, registro[12])
                    self.inpborda.insert(0, registro[10])
                    self.inpbebida.insert(0, registro[11])
        except:
            messagebox.showinfo("erro")

    def btn_DELpedi(self):
        cpf = self.inpcpf.get()
        ctrl = CtrLogin()
        ctrl.Delete_pedido(cpf)

        self.inpcpf.delete(0, END)
        self.inpnome.delete(0, END)
        self.inpNumPedido.delete(0, END)
        self.inpende.delete(0, END)
        self.inpnum.delete(0, END)
        self.inpcomp.delete(0, END)
        self.inptel.delete(0, END)
        self.inpsaborPizza.delete(0, END)
        self.inpvalor.delete(0, END)
        self.inpborda.delete(0, END)
        self.inpbebida.delete(0, END)

if __name__ == "__main__":
    main = View_home()
    main.start1()

























