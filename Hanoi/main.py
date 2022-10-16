from Hanoi import Torre

def string_torres():
    print('')
    # Torre A
    torres[0].to_string()
    # Torre B
    torres[1].to_string()
    # Torre C
    torres[2].to_string()

if __name__ == '__main__':
    print('\nBem vindo a Torre de Hanoi!')
    print('Regras: ')
    print('1 - Movimentar uma só peça (disco) de cada vez.')
    print('2 - Uma peça maior não pode ficar acima de uma menor.')
    print('3 - Não é permitido movimentar uma peça que esteja abaixo de outra.\n')

    discos_jogo = int(input('Digite quantos discos(até 10): '))
    discos = []
    i = discos_jogo
    while i > 0:
        discos.append(i)
        i -= 1
    else:
        print('Erro em inserir os discos, tente de novo!')

    torres = [Torre('A', discos), Torre('B', []), Torre('C', [])]
