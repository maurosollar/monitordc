import network, json, ssd1306, utils, dht, RTCounter
from machine import Pin, SoftI2C
from micropyserver import MicroPyServer
from time import sleep

i2c = SoftI2C(scl=Pin(32), sda=Pin(33), freq=400000) # IO33=485_EN / IO32=CFG

sensor = dht.DHT22(Pin(4))

display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Visto no site do MicroPython - Wireless-Tag's WT32-ETH01 v1.4
lan = network.LAN(mdc=Pin(23), mdio=Pin(18),
                  phy_type=network.PHY_LAN8720, phy_addr=1,
                  power=Pin(16))

if not lan.active():
    lan.active(True)

while not lan.isconnected():
    pass

sleep(3)
endip = lan.ifconfig()[0]
t_media = u_media = []
ler_sensor()


def temp_umidade(request):
    ''' rota principal '''
    global t_media
    global u_media
    temperatura = sum(t_media)/len(t_media)
    umidade = sum(t_umidade)/len(t_umidade)
    json_str = json.dumps({"temperatura": temperatura, "umidade": umidade})
    server.send("HTTP/1.0 200 OK\n")
    server.send("Content-Type: application/json\n")
    server.send("Connection: close\n\n")      
    server.send(json_str)


def ler_sensor(request)
    rtc.stop() 
    global t_media
    global u_media
    sensor.measure()
    temperatura = sensor.temperature()
    umidade = sensor.humidity()
    if len(t_media) > 5:
        t_media.pop(0)
        u_media.pop(0)
    t_media.append(temperatura)
    u_media.append(umidade)
    temp = "Temp.: " + str(temperatura)
    umid = "Umidade: " + str(umidade)
    display.fill(0)
    display.text('End. IP:', 0, 0, 1)
    display.text(endip, 0, 16, 1)
    display.text(temp, 0, 32, 1)
    display.text(umid, 0, 48, 1)
    display.show()  
    rtc.start()

rtc = RTCounter(2, period=250, mode=RTCounter.PERIODIC, callback=ler_sensor)

server = MicroPyServer()

''' add routes '''
server.add_route("/", temp_umidade)

''' start server '''
server.start()
