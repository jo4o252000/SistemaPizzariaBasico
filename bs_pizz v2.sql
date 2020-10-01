#drop database bd_pizz;

create database bd_pizz;

use bd_pizz;

#CREATE USER 'joao1'@'Localhost' IDENTIFIED BY '123456';
#GRANT SELECT, DELETE, INSERT, UPDATE, EXECUTE ON bd_pizz.* TO 'joao1'@'Localhost';

create table cad_cli(
	id_cli int primary key auto_increment not null,
    nome varchar(45) not null,
    cpf int not null,
    logradouro varchar(45) not null,
    bairro varchar(30) not null,
    num_resi int not null,
    comp_resi varchar(15) not null,
    tel_resi int not null,
    cel int not null,
    dt_cads datetime not null
);
create table log_caix(
	id_usu int primary key auto_increment not null,
    log_usu varchar(20) not null,
    senha varchar(8) not null
);
create table sbr_pizz(
	id_sbr int primary key auto_increment not null,
    sbr_pizza varchar(15) not null,
    vlr_pizza varchar(20) not null
);
create table pedi_cli(
	id_pedido int primary key auto_increment not null,
    cpf varchar(11) not null,
    nome varchar(50) not null,
    endereço varchar(50) not null,
    numero varchar(10) not null,
    complemento varchar(25) not null,
    tel varchar(8) not null,
    cel varchar(9) not null,
    sbr_pizz varchar(30) not null,
    valor varchar(10) not null,
    borda varchar(20) not null,
    bebida varchar(20) not null,
    total varchar(20) not null,
    dthr_pedido datetime default now()
   
);

insert into log_caix (log_usu, senha) value ('joão', '123456');
insert into log_caix (log_usu, senha) value ('Diego', '123456');
insert into sbr_pizz (sbr_pizza, vlr_pizza) value   ('portuguesa','45.5'),('Alho e Óleo','30.5'),('Aliche','42.5'),('Ao Funghi','52.6'), ('Atum','25.9'),('Baiana','34.8'),('Bauru','21.3'),
													('Calabresa','20.0'),('Caponesa','23.4'),('Canadense','29.4'),('Capri','32.4'),('Catupiry','32.1'),('Cubana','38.6'),('Escarola','27.6'),('Firense','30.3'),
													('Frango',27.6),('Gramute','48.6'),('Gratinada','39.2'),('Grega','38.0'),('Imperial','32.1'), ('Margherita','32.1'),('Matriciana','29.1'),('Mexicana','23.5'),
													('Napolitalho','24.5'),('Napolitano','264'),('Oba Oba','28.5'),('Palmito','25.4'), ('Portuguesa','38.5'), ('Provolone','36.5'),('Quatro Queijos','37.6'),
													('Romana','23.4'),('Rústica','32.5'),('Seciliana','23.5'),('Torino','29.5'),('Toscana','25.7'),('Veneza','49.9'),('vienense','38.4'),('Moda da Casa','29.4'),
													('Mussarela','19.5'),('Caipira','25.6');
