def classificar_transacao(valor):
    if valor < 100:
        return "pequena"
    elif valor < 1000:
        return "media"
    else:
        return "grande"