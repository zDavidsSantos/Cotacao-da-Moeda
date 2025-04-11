
import requests
from tkinter import *  #importa a biblioteca tkinter


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']


    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


janela = Tk() # inicia o tkinter
janela.title('David, veja a Cotação da Moeda.')   # titulo da janela
#janela.geometry("400x300") # tamanho da janela

texto_orientacao = Label(janela, text="Clique no Botão para ver a cotação das Moedas")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10) #pad é o espaço deixado a volta de cada elamento.

botao = Button(janela, text="Clique Aqui..", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)


texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)


 

janela.mainloop()  # esta linha gera o loop