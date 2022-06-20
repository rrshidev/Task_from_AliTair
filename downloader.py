import requests

saveFile = open(r'/home/rrshidev/Projects/ali/clientFile.xml', 'wb')
send = requests.get('http://stripmag.ru/datafeed/p5s_full_stock.xml')
saveFile.write(send.content)
saveFile.close()

saveFileFid = open(r'/home/rrshidev/Projects/ali/ourFile.xml', 'wb')
sendFid = requests.get('http://alitair.1gb.ru/Intim_Ali_allfids_2.xml')
saveFileFid.write(sendFid.content)
saveFileFid.close()
