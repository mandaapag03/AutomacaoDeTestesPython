"""Carrinho de compras feature tests."""

from pytest import fixture # type: ignore
from app.carrinho_compras import CarrinhoCompras
from pytest_bdd import ( # type: ignore
    given,
    scenario,
    then,
    when,
)

@fixture
def carrinho():
    """Fixture para criar um carrinho de compras."""
    return CarrinhoCompras()

@scenario('../features/carrinho.feature', 'Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    """Adicionar itens ao carrinho."""
    pass

@scenario('../features/carrinho.feature', 'Remover item do carrinho')
def test_remover_item_do_carrinho():
    """Remover item do carrinho."""
    pass


@given('que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99')
def adicionar_camiseta(carrinho):
    """que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99."""
    carrinho.adicionar_item('Camiseta', 29.99)


@when('eu adiciono o item "Calça" com o preço R$ 49.99')
def adicionar_calca(carrinho):
    """eu adiciono o item "Calça" com o preço R$ 49.99."""
    carrinho.adicionar_item('Calça', 49.99)

@then('o total do carrinho de compras deve ser R$ 79.98')
def total_compras(carrinho):
    """o total do carrinho de compras deve ser R$ 79.98."""
    assert carrinho.total() == 79.98


@when('eu removo o item do carrinho')
def remover_item_do_carrinho(carrinho):
    """eu removo o item do carrinho."""
    carrinho.remover_item()


@then('o carrinho de compras deve estar vazio')
def verifica_se_carrinho_esta_vazio(carrinho):
    """o carrinho de compras deve estar vazio."""
    assert carrinho.esta_vazio() == True


