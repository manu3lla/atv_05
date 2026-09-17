def transferir(origem, destino, valor):
    origem.sacar(valor)
    destino.depositar(valor)