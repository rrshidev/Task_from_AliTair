# -*- coding: utf-8 -*-
import top.api

req=top.api.AliexpressSolutionFeedSubmitRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.operation_type="PRODUCT_CREATE"
req.item_list=""
req.developer_features="{\"source\":\"Lengow\"}"
try:
	resp= req.getResponse(sessionkey)
	print(resp)
except Exception,e:
	print(e)

"""
Response Example
XML
<aliexpress_solution_feed_submit_response>
    <job_id>200000000060024475</job_id>
</aliexpress_solution_feed_submit_response>
"""

"""
Error Example
XML
<error_response>
    <code>50</code>
    <msg>Remote service error</msg>
    <sub_code>isv.invalid-parameter</sub_code>
    <sub_msg>非法参数</sub_msg>
</error_response>
"""