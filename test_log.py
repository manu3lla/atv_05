import os
import pytest
from carteira import CarteiraDigital


@pytest.fixture
def carteira_com_log():
    log_path = "carteira.log"

    if os.path.exists(log_path):
        os.remove(log_path)

    carteira = CarteiraDigital(log_path=log_path)

    yield carteira

    if os.path.exists(log_path):
        os.remove(log_path)


def test_deposito_grava_log(carteira_com_log):
    carteira = carteira_com_log
    carteira.depositar(100)
    with open("carteira.log", "r") as f:
        conteudo = f.read()
    assert conteudo == "deposito:100\n"