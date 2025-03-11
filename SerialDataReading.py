'''
  Código desenvolvido por Maria Gabriela de Miranda Porto
  
  Este projeto tem como objetivo estabelecer uma comunicação serial (USB) com um computador
  
  Foi feito um circuito com uma LED e um pushbutton a fim de indicar o estabelecimento
  bem sucedido de conexão e adicionar uma unidade à variável cujo valor será transmitido
  para o computador, respectivamente
  
'''

# PYTHON CODE
# O objetivo deste programa é ler dados transmitidos via comunicação serial

from serial import Serial, SerialException
from time import sleep

porta = "/dev/ttyUSB0"  # Ajuste conforme necessário (ex: "COM3" no Windows)

# Tentar conectar até que o ESP32 seja detectado
while True:
    try:
        ser = Serial(porta, 115200)
        print("Conectado ao ESP32!")
        break  # Sai do loop quando conectar
      
    except SerialException:
        print("Aguardando ESP32...")
        sleep(2)

# Loop para leitura de dados
while True:
    try:
        linha = ser.readline().decode('utf-8').strip() # UTF-8 corresponde ao modelo de teclado e os caracteres pertencentes à ele
        print(f"Dado recebido: {linha}")
      
    except SerialException:
        print("Erro na comunicação serial")
        break  # Encerra o programa caso haja erro crítico
