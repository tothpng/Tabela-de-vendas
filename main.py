import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2845c9b10a1d7da39a8dccdd8d958d90"
# Your Auth Token from twilio.com/console
auth_token = "073a3ef6480d1c1449d73486692d53fe"
client = Client(account_sid, auth_token)

# Abrir meus seis arquivos em Excel
lista_meses = ['01 Janeiro', '02 Fevereiro', '03 Março', '04 Abril', '05 Maio', '06 Junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        colaborador = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Colaborador'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+5573982013070",
            from_="+16266061693",
            body=f'No mês de {mes} o Colaborador {colaborador} bateu a meta com o total de Vendas de {vendas} reais.')
        print(message.sid)