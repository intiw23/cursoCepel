                    
# Python 'Hello world' program
def main():
  print("Hello world em Python")
  print(lepoesia)

def lepoesia():
  arq = open("poesia.txt")
  linhas = arq.readlines()
  for linha in linhas:
    print(linha)
 
if __name__ == '__main__':
    main()


                
