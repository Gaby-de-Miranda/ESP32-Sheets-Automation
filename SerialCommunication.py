'''
  Código desenvolvido por Maria Gabriela de Miranda Porto
  
  Este projeto tem como objetivo estabelecer uma comunicação serial (USB) com um computador
  
  Foi feito um circuito com uma LED e um pushbutton a fim de indicar o estabelecimento
  bem sucedido de conexão e adicionar uma unidade à variável cujo valor será transmitido
  para o computador, respectivamente
  
'''
# MICROPYTHON CODE

from machine import UART, Pin
from machine import UART, Pin
from time import sleep_ms as sleep
from time import ticks_ms

i = 0 # Variável a ser transmitida
j = 0 # Variável de controle
rep = 0 # Variável de repique do botão
indicador = Pin(5, Pin.OUT) # LED conectado ao pino 5
botao = Pin(4, Pin.IN, Pin.PULL_UP) # Pushbutton conectado ao pino 4

# Função de controle para o botão
def apertoubotao(pino):
    global rep 
    global i
    global j
    if ((ticks_ms()-rep) > 300):
        rep = ticks_ms()    
        i = i + 1
        j = j + 1
        
# Garante que o aperto do botão seja registrado ainda que o aperto ocorra durante o delay
botao.irq(trigger=Pin.IRQ_FALLING, handler=apertoubotao)

try:
    # Iniciando comunicação serial
    uart1 = UART(1, baudrate=115200, tx=17, rx=16)

except OSError as e:
    # Indica o erro caso a conexão seja mal sucedida
    print(f"Erro ao inicializar UART: {e}")
    
else:
    # Acende o LED caso a conexão seja bem sucedida
    indicador.value(1)
    
while True:
    # Envia apenas valores novos, evitando repetições no output do destinatário
    if (j == 1):
        print(i)
        j = j - 1
    sleep(500) # Delay de 500 milisegundos
    
