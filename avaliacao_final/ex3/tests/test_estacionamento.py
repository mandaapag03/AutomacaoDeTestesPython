"""Controle de estacionamento feature tests."""

from unittest.mock import Mock
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pytest import fixture
from src.ticket import Ticket
from src.estacionamento import Estacionamento
from datetime import datetime

@fixture
def ticket():
    return Ticket("SLA1234", "Celta", datetime(year=2024, month=5, day=18, hour=7, minute=0, second=0))

@fixture
def estacionamento():
    return Estacionamento()

@scenario('../features/estacionamento.feature', 'Emitir um ticket para a entrada do veiculo')
def test_emitir_um_ticket_para_a_entrada_do_veiculo():
    """Emitir um ticket para a entrada do veiculo."""

@given('um veiculo entra no estacionamento')
def veiculo_entra_no_estacionamento():
    """um veiculo entra no estacionamento."""
    

@when('o frentista emite um ticket para o veiculo')
def frentista_emite_ticket_para_veiculo(estacionamento, ticket):
    """o frentista emite um ticket para o veiculo."""
    estacionamento.emitir_ticket(ticket)

@then('o ticket contem informacoes corretas sobre a entrada do veiculo')
def ticket_contem_informacoes_corretas_do_carro(ticket):
    """o ticket contem informacoes corretas sobre a entrada do veiculo."""
    assert ticket.placa == "SLA1234"
    assert ticket.modelo == "Celta"
    assert ticket.entrada == datetime(year=2024, month=5, day=18, hour=7, minute=0, second=0)


@scenario('../features/estacionamento.feature', 'Calcular o valor devido para a saida de veiculo')
def test_calcular_o_valor_devido_para_a_saida_de_veiculo():
    """Calcular o valor devido para a saida de veiculo."""

@given('um veiculo esta estacionado ha 2 horas')
def veiculo_esta_estacionado_ha_2_horas():
    """um veiculo esta estacionado ha 2 horas."""
    

@when('o cliente apresenta o ticket de entrada para a saida')
def cliente_apresenta_ticket_de_entrada_para_a_saida_as_9_horas(ticket):
    """o cliente apresenta o ticket de entrada para a saida."""
    registrar_saida = Mock()
    registrar_saida.return_value = datetime(year=2024, month=5, day=18, hour=9, minute=0, second=0)
    ticket.saida = registrar_saida()


@then('o frentista calcula o valor devido corretamente')
def frentista_calcula_o_valor_devido_20_reais(estacionamento, ticket):
    """o frentista calcula o valor devido corretamente."""
    assert estacionamento.calcular_valor_devido(ticket) == 20
