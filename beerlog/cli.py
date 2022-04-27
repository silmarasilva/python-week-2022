# comand line interface
# front-end da nossa aplicação, entrega os dados para o terminal. Não são inseridas as lógicas do programa. 

from .config import settings


def main():
    print("Hello from", settings.NAME)
