import pytest
from carteira import CarteiraDigital, SaldoInsuficienteError


def test_saldo_inicial():
    carteira = CarteiraDigital()
    saldo = carteira.saldo
    assert saldo == 0


def test_saldo_inicial_com_valor():
    carteira = CarteiraDigital(100)
    saldo = carteira.saldo
    assert saldo == 100


def test_depositar():
    carteira = CarteiraDigital(100)
    carteira.depositar(50)
    assert carteira.saldo == 150


def test_sacar():
    carteira = CarteiraDigital(100)
    carteira.sacar(30)
    assert carteira.saldo == 70


def test_saque_sem_saldo_suficiente_gera_excecao():
    carteira = CarteiraDigital(100)
    with pytest.raises(SaldoInsuficienteError) as exc:
        carteira.sacar(150)
    assert str(exc.value) == "saldo insuficiente"


def test_saque_sem_saldo_suficiente_nao_altera_saldo():
    carteira = CarteiraDigital(100)
    with pytest.raises(SaldoInsuficienteError):
        carteira.sacar(150)
    assert carteira.saldo == 100