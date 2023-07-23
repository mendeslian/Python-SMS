import pandas as pd
from twilio.rest import Client

account_sid = "AC9162506b1df4a12ae9e6c57db39ecbb8"
auth_token  = "78dc1cf899f5c3b57fbb517142c59175"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            # Os números utilizados não existem, foram gerados para exemplificar a estrutura do código.
            to="+5521982323618",
            from_="+5521992144858",
            body=f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)


