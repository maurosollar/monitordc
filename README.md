# monitordc
Monitor de temperatura e umidade em Micropython utilizando o módulo WT32-ETH01 + Sensor Bosch BME280 + Display O'Led, retorna um Json: {"temperatura": 23.5, "umidade": 56.8}

Barramento i2c utilizado pelo display + sensor: SDA=Pino 33, SCL=Pino 32


Para colocar o WT32-ETH0 em modo de gravação, fechar pino IO0 e GND


Sequência:

TXD - RX da serial do micro

RXD - TX da serial do micro

IO0 - --+

        +--> Fechar
        
GND - --+


Alimentação:

3.3V

GND

Pinos i2c:

485_EN = SDA

CFG = SCL
