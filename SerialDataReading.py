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
i = 0

# Loop principal, que assegura que o código não pare mesmo em caso de interrupções
while True:
    # Loop para conexão
    while (i == 0):
        try:
            ser = Serial(porta, 115200)
            print("Conectado ao ESP32!")

            i = i + 1  # Passa para o loop de leitura de dados

        except SerialException:
            print("Aguardando ESP32...")
            sleep(2)

    # Loop para leitura de dados
    while (i == 1):
        try:
            dado = ser.readline().decode('utf-8').strip()
            print(f"Recebido: {dado}")

        except SerialException:
            print()
            print("Erro na comunicação serial!")
            print("Tentando reconectar...")
            print()
            sleep(1)

            i = i - 1 # Volta para o loop de conexão
