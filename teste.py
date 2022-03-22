print ('-' *42)
print('MENU'.center(42))
print ('-' *42)
while True:
    n = int(input('''[1] adiciona
[2] mostrar'''))
    if n == 1 :
        teste = open('teste.txt', 'a')
        palavras = input('digiter algo: ')
        teste.write('-' *len(palavras)+'\n')
        teste.write(palavras+"\n")
        teste.write('-' *len(palavras)+'\n')
        print(f'{palavras} adicionado na lista com sucesso')
    elif n == 2:
        teste = open('teste.txt', 'r')
        print(teste.read())