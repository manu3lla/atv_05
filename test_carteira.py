import pytest
from carteira import CarteiraDigital, SaldoInsuficienteError


def test_saldo_inicial():
    # Arrange
    carteira = CarteiraDigital()

    # Act
    saldo = carteira.saldo

    # Assert
    assert saldo == 0


def test_saldo_inicial_com_valor():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    saldo = carteira.saldo

    # Assert
    assert saldo == 100


def test_depositar():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    carteira.depositar(50)

    # Assert
    assert carteira.saldo == 150


def test_sacar():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    carteira.sacar(30)

    # Assert
    assert carteira.saldo == 70


def test_saque_sem_saldo_suficiente_gera_excecao():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    with pytest.raises(SaldoInsuficienteError) as exc:
        carteira.sacar(150)

    # Assert
    assert str(exc.value) == "saldo insuficiente"


def test_saque_sem_saldo_suficiente_nao_altera_saldo():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    with pytest.raises(SaldoInsuficienteError):
        carteira.sacar(150)

    # Assert
    assert carteira.saldo == 100