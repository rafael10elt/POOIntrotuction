# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""

#Programação Orientada a Objetos
#Classes e Objetos

class Livro():
  #O self indica que estes são atributos dos objetos
  def __init__ (self):# o metodo init é o construtor da classe
    self.titulo = 'O monge e o executivo'#O self indica que estes são atributos dos objetos
    self.isbn = 9988888
    print('Contrutor chamado para criar um objeto desta classe')
 
  #Métodos são funções, que recebem como parametro atributos do objeto criado
  def imprime(self):
    print('Foi criado o livro %s e ISBN %d' %(self.titulo, self.isbn))

#Cirando uma instancia da classe livro
Livro1 = Livro()

#Atributo do Objeto Livro1
Livro1.titulo

#Metodo do Objeto Livro1
Livro1.imprime()

#Criando a classe Livro com  parametros no metodo construtor
class Livro():
  #O self indica que estes são atributos dos objetos
  def __init__ (self):# o metodo init é o construtor da classe
    self.titulo = titulo
    self.isbn = isbn
    print('Contrutor chamado para criar um objeto desta classe')

  def imprime(self):
    print('Foi criado o livro %s e ISBN %d' %(self.titulo, self.isbn))

#Criando o objeto Livro2 que é uma instancia da classe Livro
Livro2 = Livro("A menina que roubava livros", 77886611)
Livro2.titulo
Livro2.imprime('A menina que roubava livros', 77886611)

#Criando a classe cachorro
class cachorro():
  def __init__(self, raca):
    self.raca = raca
    print("Contrutor chamado para criar um objeto desta classe")

#Criando um objeto a partir da classe cachorro
Rex = Cachorro(raca='Labrador')

#Criando um objeto a partir da classe cachorro
Alvinho = Cachorro(raca='Yorkshire')

#Atributo da classe cachorro, utilizado pelo objeto criado
Rex.raca
Alvinho.raca