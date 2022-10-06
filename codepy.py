                    
# Python 'Hello world' program
import sys

def main():
    nome = "poesia.txt"
    #print("Hello world em Python")
    lepoesias(nome)


def lepoesia():
    arq = open("poesia.txt")
    linhas = arq.readlines()
    for linha in linhas:
        print(linha)

def lepoesias(nome):
    with open(nome, 'r', encoding='utf-8') as arq_entrada:
        # CORPO DO WITH
        conteudo = arq_entrada.read()

    # continue o programa usando conteudo
    print(conteudo)

if __name__ == '__main__':
    main()

                
