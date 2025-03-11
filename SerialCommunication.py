# MICROPYTHON CODE

'''
  Código desenvolvido por Maria Gabriela de Miranda Porto
  
  Este projeto tem como objetivo estabelecer uma comunicação serial (USB) com um computador
  
  Foi feito um circuito com uma LED e um pushbutton a fim de indicar o estabelecimento
  bem sucedido de conexão e adicionar uma unidade à variável cujo valor será transmitido
  para o computador, respectivamente
  
'''

from machine import UART, Pin
from time import sleep, ticks_ms

i = 0 # Variável que será repassada
rep = 0 # Repique do pushbutton

indicador = Pin(5, Pin.OUT) # LED
botao = Pin(4, Pin.IN, Pin.PULL_UP) # Pushbutton

# Função que registra o aperto do botão e muda o valor de i
def apertoubotao(pino):
    global rep
    global i 
    if ((ticks_ms() - rep) > 300):
        rep = ticks_ms()    
        i += 1
      
botao.irq(trigger=Pin.IRQ_FALLING, handler=apertoubotao)

try:
    # Iniciando a comunicação serial
    uart1 = UART(1, baudrate=115200, tx=17, rx=16)
except OSError as e:
    print(f"Erro ao inicializar UART: {e}")  
else:
    # Liga a LED caso a conexão seja bem sucedida
    indicador.value(1)
    
while True:
    print(i)
    sleep(2)
