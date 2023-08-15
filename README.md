# monitordc
Monitor de temperatura e umidade em Micropython utilizando o módulo WT32-ETH01 + Sensor Bosch BME280 + Display O'Led, retorna um Json Ex.: {"temperatura": 23.5, "umidade": 56.8}


```
Para colocar o WT32-ETH0 em modo de gravação, fechar pino IO0 e GND

Instalar o Python 3
Instalar ferramenta esptool: pip install esptool
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin


Sequência:
TXD - RX da serial do micro
RXD - TX da serial do micro
IO0 - ---\
          |--> Fechar para entrar em modo de gravação
GND - ---/

Alimentação:
3.3V
GND

Pinos i2c:
485_EN = SDA
CFG = SCL

```
