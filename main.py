import machine, esp32, network, json, ssd1306, utils, dht
from machine import Pin, SoftI2C
from micropyserver import MicroPyServer
from time import sleep

i2c = SoftI2C(scl=Pin(32), sda=Pin(33), freq=400000) # IO33=485_EN / IO32=CFG

sensor = dht.DHT22(machine.Pin(4))

display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Visto no site do MicroPython - Wireless-Tag's WT32-ETH01 v1.4
lan = network.LAN(mdc=machine.Pin(23), mdio=machine.Pin(18),
                  phy_type=network.PHY_LAN8720, phy_addr=1,
                  power=machine.Pin(16))

if not lan.active():
    lan.active(True)

while not lan.isconnected():
    pass

sleep(3)
endip = lan.ifconfig()[0]
sensor.measure()
temperatura = sensor.temperature()
umidade = sensor.humidity()
json_str = json.dumps({"temperatura": temperatura, "umidade": umidade})
temp = "Temp.: " + str(temperatura)
umid = "Umidade: " + str(umidade)
display.fill(0)
display.text('End. IP:', 0, 0, 1)
display.text(endip, 0, 16, 1)
display.text(temp, 0, 32, 1)
display.text(umid, 0, 48, 1) 
display.show()


def temp_umidade(request):
    ''' rota principal '''
    sensor.measure()
    temperatura = sensor.temperature()
    umidade = sensor.humidity()
    json_str = json.dumps({"temperatura": temperatura, "umidade": umidade})
    temp = "Temp.: " + str(temperatura)
    umid = "Umidade: " + str(umidade)
    display.fill(0)
    display.text('End. IP:', 0, 0, 1)
    display.text(endip, 0, 16, 1)
    display.text(temp, 0, 32, 1)
    display.text(umid, 0, 48, 1)
    display.show()
    server.send("HTTP/1.0 200 OK\n")
    server.send("Content-Type: application/json\n")
    server.send("Connection: close\n\n")      
    server.send(json_str)
    
def mensagem_display(request):
    ''' rota display '''
    # http://IP/mostra?mensagem=Teste
    params = utils.get_request_query_params(request)
    mensagem = params["mensagem"]
    display.fill(0)
    display.text('End. IP:', 0, 0, 1)
    display.text(endip, 0, 16, 1)
    display.text(mensagem, 0, 34, 1)
    display.show()
    server.send("Mensagem enviada para o display: " + mensagem)

server = MicroPyServer()

''' add routes '''
server.add_route("/", temp_umidade)
server.add_route("/mostra", mensagem_display)

''' start server '''
server.start()

