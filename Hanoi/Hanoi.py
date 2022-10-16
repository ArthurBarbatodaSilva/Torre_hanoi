class Torre:
    def init(self, torre, discos):
        self._torre = torre
        self._discos = discos

    def tirar_disco(self):
        return self._discos.pop()

    def get_tamanho(self):
        return len(self._discos)

    def primeiro_disco(self):
        return self._discos[0]

    def torre(self):
        return self._torre

    def to_string(self):
        print('Torre: ' + self._torre)