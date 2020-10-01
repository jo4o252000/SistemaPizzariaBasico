import pymysql

class ConectaBanco: #define a classe
    def __init__(self): #init é o metodo inicializador de classe
        self.con = ""    #cria a variavel de conexão vazia
    def conecta(self): #metodo para conectar no banco
        host = "localhost"
        user = "adminc"
        password = "123admin"
        db = "bd_pizz"
        port = 3306
        self.con = pymysql.connect(host, user, password, db, port)
    def select (self, campos, tabelas, where=None, And=None):
        self.conecta()
        cur = self.con.cursor() #cria uma variavel do tipo cursor que permite executar query sql
        query = ("SELECT " + campos + " FROM " + tabelas)
        if where: #caso tenha um parametro where
            query = (query + " WHERE " + where)
        if And:
            query = (query + " and " + And)
        print(query)
        cur.execute(query)
        result = cur.fetchall()
        self.con.close()
        return result
    def insert (self, tabela,valores, campos=None):
        self.conecta()
        cur = self.con.cursor()
        query = ("INSERT INTO " + tabela)
        if campos: #caso haja especificação de campos
            query = (query+"(" + campos + ")")
        query = (query + " values(" + valores + ");")
        print(query)
        cur.execute(query)
        self.con.commit()# executa o commit
        self.con.close()# encerra a conexão com o banco
    def update (self, tabela, sets, where=None):
        self.conecta()
        cur = self.con.cursor()
        query = ("UPDATE" + tabela + "SET" + sets)
        if where:
            query = (query + "WHERE" + where)
        print(query)
        cur.execute(query)
        self.con.commit()
        self.con.close()
    def delete (self, tabela, where):
        self.conecta()
        cur = self.con.cursor()
        query = ("DELETE FROM " + tabela + " WHERE " + where)
        print(query)
        cur.execute(query)
        self.con.commit()
        self.con.close()



