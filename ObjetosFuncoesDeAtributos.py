# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""

#Objetos e funções de atributos

#Criando uma classe
class funcionarios:
  def __init__(self,nome, salario):
    self.nome = nome
    self.salario = salario
  
  def listFunc(self):
    print("O nome do funcionario é "+self.nome+" e o salario é R$ "+ str(self.salario))

#Criando um objeto chamado Func1 a partir da classe Funcionarios
Func1 = funcionarios("Rafa", 20000)

#Usando o método classe
Func1.listFunc()

print("****Usando atributos ****")

hasattr(Func1, 'nome')#hasattr , tem o atributo 'nome'?(true ou false) em Func1

hasattr(Func1, 'salario')

setattr(Func1, 'salario', 4500)#configura o atributo 'salario' em Func1

hasattr(Func1, 'salario')

getattr(Func1, 'salario')#oegue o atributo ' salario' em Func1

delattr(Func1, 'salario')#Delete o atributo ' salario em Func1

hasattr(Func1, 'salario')