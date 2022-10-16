class Torre:
    def init(self, torre, discos):
        self._torre = torre
        self._discos = discos

    def colocar_disco(self, disco):
        if self.get_tamanho() == 0:
            self._discos.append(disco)
        else:
            if int(self.ultimo_disco()) > disco:
                self._discos.append(disco)
            else:
                print('Não é possivel inserir esse disco, o disco abaixo é menor')

    def tirar_disco(self):
        return self._discos.pop()

    def get_tamanho(self):
        return len(self._discos)

    def ultimo_disco(self):
        return self._discos[len(self._discos) - 1]

    def primeiro_disco(self):
        return self._discos[0]

    def torre(self):
        return self._torre

    def to_string(self):
        print('Torre: ' + self._torre)

        for disco in list(reversed(self._discos)):
            print(disco)