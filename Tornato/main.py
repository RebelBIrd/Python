import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import threading
import requests
import time
import json
import random

from datetime import datetime

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [(r"/todayProfit", TodayProfit),
					(r"/historyProfit", HistoryProfit),
					(r"/ticketPresent", TicketPresent),
					(r"/spotPeople", SpotPeople),
					(r"/spotHeat", SpotHeat),
					(r"/cableway", Cableway),
					(r"/visitorTrend", VisitorTrend),
					(r"/visitorForecast", VisitorForecast),
					(r"/innerCitySource", InnerCitySource),
					(r"/outerCityPercent", OuterCityPercent),
					(r"/parkInfomation", ParkInfomation),
					(r"/", WelComePage)]
		tornado.web.Application.__init__(self, handlers, debug=True)

class TodayProfit(tornado.web.RequestHandler):
	def get(self):
		self.finish({
			'code': 1,
			'result': {
				'sum': 31585,
				'date': '2017.10.22',
				'presents': [
				    { 'name': '网络销售', 'sum': random.randint(1000, 5000) },
				    { 'name': '传销', 'sum': 4551 },
				    { 'name': '强卖', 'sum': 8786 },
				    { 'name': '门店销售', 'sum': 936 },
				    { 'name': '送出', 'sum': 3323 },
				    { 'name': '抽奖', 'sum': 3592 }]
   					}
			})

class HistoryProfit(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
			        { 'date': "2017-10-1", 'num': 9593 }, 
			        { 'date': "2017-10-2", 'num': 6278 }, 
			        { 'date': "2017-10-3", 'num': 11974 }, 
			        { 'date': "2017-10-4", 'num': 5987 }, 
			        { 'date': "2017-10-5", 'num': 9795 }, 
			        { 'date': "2017-10-6", 'num': 11926 }, 
			        { 'date': "2017-10-7", 'num': 6082 }, 
			        { 'date': "2017-10-8", 'num': 9013 }, 
			        { 'date': "2017-10-9", 'num': 11817 }, 
			        { 'date': "2017-10-10", 'num': 11588 }, 
			        { 'date': "2017-10-11", 'num': 6606 }, 
			        { 'date': "2017-10-12", 'num': 8924 }, 
			        { 'date': "2017-10-13", 'num': 7870 }, 
			        { 'date': "2017-10-14", 'num': 5105 }, 
			        { 'date': "2017-10-15", 'num': 8240 }, 
			        { 'date': "2017-10-16", 'num': 8750 }, 
			        { 'date': "2017-10-17", 'num': 6161 }, 
			        { 'date': "2017-10-18", 'num': 10130 }, 
			        { 'date': "2017-10-19", 'num': 5108 }, 
			        { 'date': "2017-10-20", 'num': 10170 }, 
			        { 'date': "2017-10-21", 'num': 6882 }, 
			        { 'date': "2017-10-22", 'num': 5194 }, 
			        { 'date': "2017-10-23", 'num': 9071 }, 
			        { 'date': "2017-10-24", 'num': 11158 }, 
			        { 'date': "2017-10-25", 'num': 5908 }, 
			        { 'date': "2017-10-26", 'num': 7067 }, 
			        { 'date': "2017-10-27", 'num': 11006 }, 
			        { 'date': "2017-10-28", 'num': 5459 }, 
			        { 'date': "2017-10-29", 'num': 10964 }, 
			        { 'date': "2017-10-30", 'num': 10021 }
    			]
			})

class TicketPresent(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
				{ 'name': '黄牛票', 'sum': 24864 },
		        { 'name': '正规票', 'sum': 15668 },
		        { 'name': '无座票', 'sum': 24383 },
		        { 'name': '翻墙票', 'sum': 19512 },
		        { 'name': '学生票', 'sum': 13951 },
		        { 'name': '老年票', 'sum': 31232 }]
			})

class SpotPeople(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 
			            'name': '总入园人数',
			            'sum': 83992,
			            'timePoints': [3037 ,5606 ,3876 ,6164 ,3572 ,5165 ,5418 ,4128 ,5878 ,3350 ,4351 ,4621 ,5799 ,6300 ,5665 ,5804 ,5258] 
			        },
			        { 
			            'name': '外双溪人数',
			            'sum': 57749,
			            'timePoints': [3889 ,5083 ,3003 ,5467 ,2141 ,5788 ,1930 ,3024 ,2444 ,3819 ,1877 ,2074 ,2879 ,4940 ,3128 ,3948 ,2315] 
			        },
			        { 
			            'name': '金沙人数',
			            'sum': 44955,
			            'timePoints': [4743 ,1230 ,2880 ,2195 ,1985 ,4877 ,1535 ,3360 ,1579 ,2969 ,1325 ,1898 ,3202 ,1410 ,3758 ,4100 ,1909] 
			        }
				]
			})

class SpotHeat(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 'name': '阎王殿', 'id': '001', 'num': 110, 'x': 0.2, 'y': 0.2 },
                    { 'name': '凌霄殿', 'id': '002', 'num': 119, 'x': 0.4, 'y': 0.3 },
                    { 'name': '南天门', 'id': '003', 'num': 911, 'x': 0.5, 'y': 0.6 },
                    { 'name': '遣云宫', 'id': '004', 'num': 120, 'x': 0.7, 'y': 0.1 },
                    { 'name': '玉清宫', 'id': '005', 'num': 10086, 'x': 0.8, 'y': 0.9 }]
			})

class Cableway(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': {
			        'sumTicket': random.randint(4000, 6000),
			        'minTicket': random.randint(200,1000),
			        'maxTicket': random.randint(2000, 4000),
    			}
			})

class VisitorTrend(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 'date': "2017-10-1", 'num': 9593 }, 
		            { 'date': "2017-10-2", 'num': 6278 }, 
		            { 'date': "2017-10-3", 'num': 11974 }, 
		            { 'date': "2017-10-4", 'num': 5987 }, 
		            { 'date': "2017-10-5", 'num': 9795 }, 
		            { 'date': "2017-10-6", 'num': 11926 }, 
		            { 'date': "2017-10-7", 'num': 6082 }, 
		            { 'date': "2017-10-8", 'num': 9013 }, 
		            { 'date': "2017-10-9", 'num': 11817 }, 
		            { 'date': "2017-10-10", 'num': 11588 }, 
		            { 'date': "2017-10-11", 'num': 6606 }, 
		            { 'date': "2017-10-12", 'num': 8924 }, 
		            { 'date': "2017-10-13", 'num': 7870 }, 
		            { 'date': "2017-10-14", 'num': 5105 }, 
		            { 'date': "2017-10-15", 'num': 8240 }, 
		            { 'date': "2017-10-16", 'num': 8750 }, 
		            { 'date': "2017-10-17", 'num': 6161 }, 
		            { 'date': "2017-10-18", 'num': 10130 }, 
		            { 'date': "2017-10-19", 'num': 5108 }, 
		            { 'date': "2017-10-20", 'num': 10170 }, 
		            { 'date': "2017-10-21", 'num': 6882 }, 
		            { 'date': "2017-10-22", 'num': 5194 }, 
		            { 'date': "2017-10-23", 'num': 9071 }, 
		            { 'date': "2017-10-24", 'num': 11158 }, 
		            { 'date': "2017-10-25", 'num': 5908 }, 
		            { 'date': "2017-10-26", 'num': 7067 }, 
		            { 'date': "2017-10-27", 'num': 11006 }, 
		            { 'date': "2017-10-28", 'num': 5459 }, 
		            { 'date': "2017-10-29", 'num': 10964 }, 
		            { 'date': "2017-10-30", 'num': 10021 }
				]
			})

class VisitorForecast(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 'date': "2017-10-1", 'num': 9593 }, 
		            { 'date': "2017-10-2", 'num': 6278 }, 
		            { 'date': "2017-10-3", 'num': 11974 }, 
		            { 'date': "2017-10-4", 'num': 5987 }, 
		            { 'date': "2017-10-5", 'num': 9795 }, 
		            { 'date': "2017-10-6", 'num': 11926 }, 
		            { 'date': "2017-10-7", 'num': 6082 }, 
		            { 'date': "2017-10-8", 'num': 9013 }, 
		            { 'date': "2017-10-9", 'num': 11817 }, 
		            { 'date': "2017-10-10", 'num': 11588 }, 
		            { 'date': "2017-10-11", 'num': 6606 }, 
		            { 'date': "2017-10-12", 'num': 8924 }, 
		            { 'date': "2017-10-13", 'num': 7870 }, 
		            { 'date': "2017-10-14", 'num': 5105 }, 
		            { 'date': "2017-10-15", 'num': 8240 }, 
		            { 'date': "2017-10-16", 'num': 8750 }, 
		            { 'date': "2017-10-17", 'num': 6161 }, 
		            { 'date': "2017-10-18", 'num': 10130 }, 
		            { 'date': "2017-10-19", 'num': 5108 }, 
		            { 'date': "2017-10-20", 'num': 10170 }, 
		            { 'date': "2017-10-21", 'num': 6882 }, 
		            { 'date': "2017-10-22", 'num': 5194 }, 
		            { 'date': "2017-10-23", 'num': 9071 }, 
		            { 'date': "2017-10-24", 'num': 11158 }, 
		            { 'date': "2017-10-25", 'num': 5908 }, 
		            { 'date': "2017-10-26", 'num': 7067 }, 
		            { 'date': "2017-10-27", 'num': 11006 }, 
		            { 'date': "2017-10-28", 'num': 5459 }, 
		            { 'date': "2017-10-29", 'num': 10964 }, 
		            { 'date': "2017-10-30", 'num': 10021 }
				]
			})

class InnerCitySource(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{'name': '赣州市', 'value': 1399, 'date': '2017.10.22'},
			        {'name': '吉安市', 'value': 329, 'date': '2017.10.22'},
			        {'name': '上饶市', 'value': 152, 'date': '2017.10.22'},
			        {'name': '九江市', 'value': 299, 'date': '2017.10.22'},
			        {'name': '抚州市', 'value': 879, 'date': '2017.10.22'},
			        {'name': '宜春市', 'value': 5200, 'date': '2017.10.22'},
			        {'name': '南昌市', 'value': 999, 'date': '2017.10.22'},
			        {'name': '景德镇市', 'value': 352, 'date': '2017.10.22'},
			        {'name': '萍乡市', 'value': 9119, 'date': '2017.10.22'},
			        {'name': '鹰潭市', 'value': 3239, 'date': '2017.10.22'},
			        {'name': '新余市', 'value': 830, 'date': '2017.10.22'},]
			})

class OuterCityPercent(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 'name': '北京', 'value': 2320 },
                    { 'name': '上海', 'value': 2534 },
                    { 'name': '广州', 'value': 7643 },
                    { 'name': '东莞', 'value': 9999 },
                    { 'name': '深圳', 'value': 1234 },
                    { 'name': '成都', 'value': 520 },
                    { 'name': '厦门', 'value': 8697 },
                    { 'name': '黑龙江', 'value': 3457 },
                    { 'name': '昆明', 'value': 2445 },
                    { 'name': '大理', 'value': 6460 }]
			})

class ParkInfomation(tornado.web.RequestHandler):
	def get(self):
		car1total = random.randint(5000, 7000)
		car1used = random.randint(3000, 4000)
		car1rest = car1total - car1used
		car2total = random.randint(5000, 7000)
		car2used = random.randint(3000, 4000)
		car2rest = car1total - car1used
		car3total = random.randint(5000, 7000)
		car3used = random.randint(3000, 4000)
		car3rest = car1total - car1used
		self.finish({
				'code': 1,
				'result': [
					{ 
					'parkName': '九道口停车场',
					'total': car1total,
					'used': car1used,
					'rest': car1rest,
					'detail': [
							{ 'name': '阎王殿卡口', 'data': [1080, 2048] },
							{ 'name': '南天门卡口', 'data': [526, 346] },
							{ 'name': '凌霄殿卡口', 'data': [123, 4124] },
							{ 'name': '三清宫卡口', 'data': [15757, 12398] }
						]
					},
					{ 
					'parkName': '沙坪坝停车场',
					'total': car2total,
					'used': car2used,
					'rest': car2rest,
					'detail': [
							{ 'name': '广寒宫卡口', 'data': [545, 9578958] },
							{ 'name': '琼花宫卡口', 'data': [526, 346] },
							{ 'name': '灵官殿卡口', 'data': [49, 5795] },
							{ 'name': '宝光殿卡口', 'data': [589, 57] }
						]
					},
					{ 
					'parkName': '石碾盘停车场',
					'total': car3total,
					'used': car3used,
					'rest': car3rest,
					'detail': [
							{ 'name': '遣云宫卡口', 'data': [123, 2048] },
							{ 'name': '毗沙宫卡口', 'data': [5124, 5124] },
							{ 'name': '五明宫卡口', 'data': [12124123, 4124] },
							{ 'name': '化乐宫卡口', 'data': [123, 124124] }
						]
					}
				]
			})
		
class WelComePage(tornado.web.RequestHandler):
	"""docstring for  WelComePage"""
	def get(self):
		self.write("<h3>大黄的测试服务器</h3>")
		

if __name__ == '__main__':
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()