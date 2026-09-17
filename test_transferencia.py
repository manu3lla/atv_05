import pytest
from carteira import CarteiraDigital, SaldoInsuficienteError
from transferencia import transferir


@pytest.fixture
def carteiras():
    origem = CarteiraDigital(1000)
    destino = CarteiraDigital(0)

    return origem, destino


@pytest.mark.parametrize(
    "valor",
    [100, 250, 500],
    ids=[
        "transferencia_100",
        "transferencia_250",
        "transferencia_500",
    ]
)
def test_transferencia_sucesso(carteiras, valor):
    origem, destino = carteiras
    transferir(origem, destino, valor)
    assert origem.saldo == 1000 - valor
    assert destino.saldo == valor


def test_transferencia_maior_que_saldo_nao_altera_carteiras(carteiras):
    origem, destino = carteiras
    saldo_origem = origem.saldo
    saldo_destino = destino.saldo
    with pytest.raises(SaldoInsuficienteError):
        transferir(origem, destino, 1500)
    assert origem.saldo == saldo_origem
    assert destino.saldo == saldo_destino