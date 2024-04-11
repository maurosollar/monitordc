import network, machine, time, requests

pin12 = machine.Pin(12, machine.Pin.OUT)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

ip_servidor = '10.0.0.110'
camera = 'adm_20'

while True:
    t = time.ticks_ms()
    ap = sta_if.scan()
    pin12.value(1)    
    intenso = False
    lista_ap = ''
    for dap in ap:
        if dap[3] >= -55:
            linha = 'AP: ' + f'{dap[0].decode('ascii'):20}' + ' Canal: ' + f'{dap[2]:2}' + ' RSSI: ' + str(dap[3])
            if not str(dap[0].decode('ascii')) in 'TIHacker-RangersVisitantesRCA' or len(dap[0]) == 0:
                lista_ap = lista_ap + linha + '\n'
                intenso = True
    print('')
    if intenso:
        pin12.value(0)
        print('Sinal intenso!')
        print(lista_ap.replace(' ','').replace(':',': ').replace('Canal:', ' Canal:').replace('RSSI:', ' RSSI:'))
        urlx = "http://10.0.0.210:6060/snap?servidor=" + ip_servidor + "&camera=" + camera + "&listaap=" + lista_ap.replace(' ','').replace('\n','----').replace(':', ':%20')
        try:
            resp = requests.get(url=urlx, timeout=10)
        except:
            print('Erro conectando')
            continue
    print('Scan:', time.ticks_diff(time.ticks_ms(), t), 'ms\n')

