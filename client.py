
import time
import socket
import datetime
from dateutil import parser
from timeit import default_timer as timer
 
# Algoritmo de Cristian - Cliente
def client():

  # Cria o socket
  s = socket.socket()          
      
  # conecta com o servidor local na porta 8000
  s.connect(('127.0.0.1', 8000))

  # timestamp do envio da requisição
  hora_requisicao = timer()

  # recebe a hora do servidor
  hora_ntp = parser.parse(s.recv(1024).decode())

  # timestamp do recebimento da resposta
  hora_resposta = timer()

  # timestamp do horário atual do cliente antes da atualização
  hora_atual = datetime.datetime.now()

  print("Hora retornada pelo servidor: " + str(hora_ntp))

  #delay é a diferença entre a hora da resposta e da requisição
  delay = hora_resposta - hora_requisicao
  print("Latência: " + str(delay) + " segundos")

  # hora do cliente é a hora do servidor + o delay 
  hora_cliente = hora_ntp + datetime.timedelta(seconds = delay)

  print("Horário: " + str(hora_cliente))

  # calcula a diferença na sincronização
  diferenca = hora_atual - hora_cliente
  print("Diferença de sincronização : "+ str(diferenca.total_seconds()) + " segundos")
  return delay, diferenca
  s.close()       
 

if __name__ == '__main__':

  minutos = 0.5 # Tempo em minutos para sincronizar novamente

  iterador = 1 # Número de vezes que o cliente vai sincronizar
  total_delay = 0
  total_diferenca = 0

  while True:
    print("Iteração: " + str(iterador))
    delay, diferenca = client()
    total_delay += delay
    total_diferenca += diferenca.total_seconds()
    print("Média de latência: " + str(total_delay/iterador) + " segundos")
    print("Média de diferença de sincronização: " + str(total_diferenca/iterador) + " segundos")
    print("--------------------------------------------------")
    iterador += 1
    time.sleep(60*minutos) # Espera minutos para sincronizar novamente