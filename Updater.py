# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from top import api, appinfo
import pprint

url = 'gw.api.taobao.com'
port =

appkey = 'xxxxxxxx'
secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

req = api.AliexpressSolutionOrderGetRequest(url, port)
req.set_app_info(appinfo(appkey, secret))

req.param0 = {
'create_date_start': (datetime.utcnow() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'),
'page_size': 50,
'current_page': 1
}

#https://oauth.aliexpress.com/authorize?response_type=token&client_id=xxxxxxxx&state=1212&view=web&sp=ae
sessionkey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

resp = req.getResponse(sessionkey)
pprint.pprint(resp['aliexpress_solution_order_get_response']['result'])