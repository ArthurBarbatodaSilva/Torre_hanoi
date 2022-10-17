from Hanoi import Torre
def fim():
    print('Parabéns você ganhou, tente agora com mais discos!')

def inicio(movimentos):
    # ‘Loop’ infinito para verificar se a Torre A e a Torre B estão vazias
    # Se estiverem vazias vai para a função fim
    # Se não estiverem voltam para a função Mover
    while True:
        print('Número minimo para resolver utilizando ' + str(inicial) + ' discos: ' + str(
            2 ** inicial - 1) + ' movimentos!')
        print('Movimentos: ' + str(movimentos))
        movimentos += 1
        if torres[0].get_tamanho() == 0 and torres[1].get_tamanho() == 0:
            fim()
            break
        string_torres()
        print('Torre A = 1, Torre B = 2 e Torre C = 3')
        mover_disco(str(input('Digite a Torre de origem: ')), str(input('Digite a Torre para destino: ')))
def string_torres():
    print('')
    # Torre A
    torres[0].to_string()
    # Torre B
    torres[1].to_string()
    # Torre C
    torres[2].to_string()

def mover_disco(origemTorre, destinoTorre):
    origemTorre = torres[int(origemTorre) - 1]
    destinoTorre = torres[int(destinoTorre) - 1]

    if destinoTorre.colocar_disco(origemTorre.ultimo_disco()) == False:
        inicio(movimentos)
    origemTorre.tirar_disco()


if __name__ == '__main__':
    print('\nBem vindo a Torre de Hanoi!')
    print('Regras: ')
    print('1 - Movimentar uma só peça (disco) de cada vez.')
    print('2 - Uma peça maior não pode ficar acima de uma menor.')
    print('3 - Não é permitido movimentar uma peça que esteja abaixo de outra.\n')

    # Pergunta quantos discos a pessoa quer jogar, criamos a variavel disco vazia
    # Se o discos forem menores que 8, fazemos um append passando o i que recebeu os discos
    # No final do While colocamos ele para receber menos 1 para decrementar o valor
    # Fazendo assim inserir os disco decrescente ex(3 discos, base 3; meio 2; topo 1)

    discos_jogo = int(input('Digite quantos discos(até 10): '))
    discos = []
    i = discos_jogo
    while i > 0:
        discos.append(i)
        i -= 1

    torres = [Torre('A', discos), Torre('B', []), Torre('C', [])]
    inicial = torres[0].primeiro_disco()
    movimentos = 0
    inicio(movimentos)
