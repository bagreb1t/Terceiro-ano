# class Pessoa:
#     def falar (self):
#         print('estou falando')

#     def andar (self):
#         print('estou andando')

#     def dormir(self):
#         print('fui zzzzzz')

#     def pular(self):
#         print('Consigo saltar 10 metros')



















class Pessoa:
    def __init__ (self, nome, idade, comendo=False, falando=False, dormir=False):
        self.nome= nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormir = dormir

        
    def falar (self):
        print(f'aqui é o {self.nome} estou falando')

    def andar (self):
        print(f'Apesar de minha idade ser {self.idade} anos, estou andando')

    def comer (self,alimento):
        print(f'{self.nome}, já está comendo , {alimento}')
        self.comendo=True
        
        
        

    
