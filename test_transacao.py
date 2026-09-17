import pytest
from transacao import classificar_transacao


@pytest.mark.parametrize(
    "valor, esperado",
    [
        (50, "pequena"),
        (99, "pequena"),
        (100, "media"),
        (500, "media"),
        (999, "media"),
        (1000, "grande"),
    ],
    ids=[
        "valor_pequeno",
        "limite_antes_media",
        "limite_media",
        "valor_medio",
        "limite_antes_grande",
        "limite_grande",
    ]
)
def test_classificar_transacao(valor, esperado):
    valor_teste = valor
    resultado = classificar_transacao(valor_teste)
    assert resultado == esperado