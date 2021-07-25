# Gerador de Casos de Teste para a Questão C
from random import randint

n = 200
commands = [
    lambda x: f'insert {x}',
    lambda x: f'getMin {x}',
    lambda x: 'removeMin'
]

print(n, *[commands[randint(0,2)](randint(-5, 15)) for _ in range(n)], sep='\n')