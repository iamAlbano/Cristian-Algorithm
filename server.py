import socket
import ntplib
from datetime import datetime, timezone

# Função para obter a hora do servidor NTP
def getNTPTime():
  ntp = ntplib.NTPClient()
  response = ntp.request('pool.ntp.org', version=3)
  return datetime.fromtimestamp(response.tx_time)
   
# Algoritmo de Cristian - Servidor
def servidor():
 
  # Cria o socket
  s = socket.socket()

  # Define o endereço e a porta do servidor 8000
  s.bind(('', 8000))
    
  # Função para ouvir as conexões
  s.listen(5)     
  print("Servidor ativo para conexões")
      
  # Loop infinito para aceitar conexões
  while True:
      
    # Aceita conexões com clientes
    conexao, endereco = s.accept()     
    print('Server conectado com ', endereco)

    try:
      hora = getNTPTime()
    except:
      print("Erro ao obter a hora do servidor NTP")
      hora = datetime.datetime.now()
    
    # Envia a hora atual para o cliente
    conexao.send(str(hora).encode())
    
    # Fecha a conexão com o cliente
    conexao.close()
 
 

if __name__ == '__main__':
  servidor()