# A palavra dunder foi criada para identificar o duplo underline. Quando ouvir dunder estamos dizendo um identficador com dois underlines no começo e dois no final. Ex. dunder main.

# O arquivo main é o entrepoint, onde o programa incia a sua execução.

#geralmente nesse arquivo não é inserido muita lógica. Ele fica mais agnóstico. A lógica é colocada no arquivo CLI Outras linguagens de programação ao invez da função ou do if, criam um arquivo chamado main.

from .cli import main

if __name__ == "__main__":
    main()
