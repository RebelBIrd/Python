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
				'sum': 3010,
				'date': '2018.04.22',
				'presents': [
				    { 'name': '去哪儿', 'sum': 521 },
				    { 'name': '窗口售票', 'sum': 1230 },
				    { 'name': '携程', 'sum': 786 },
				    { 'name': '驴妈妈', 'sum': 936 },
				    { 'name': '微信', 'sum': 323 }]  
   					}
			})

class HistoryProfit(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
				    { 'date': "2018-03-26", 'num': 2115 }, 
			        { 'date': "2018-03-27", 'num': 1908 }, 
			        { 'date': "2018-03-28", 'num': 3700 }, 
			        { 'date': "2018-03-29", 'num': 1006 }, 
			        { 'date': "2018-03-30", 'num': 5459 }, 
			        { 'date': "2018-03-31", 'num': 6964 }, 
			        { 'date': "2018-04-1", 'num': 4593 }, 
			        { 'date': "2018-04-2", 'num': 6278 }, 
			        { 'date': "2018-04-3", 'num': 4974 }, 
			        { 'date': "2018-04-4", 'num': 4987 }, 
			        { 'date': "2018-04-5", 'num': 3795 }, 
			        { 'date': "2018-04-6", 'num': 6926 }, 
			        { 'date': "2018-04-7", 'num': 6082 }, 
			        { 'date': "2018-04-8", 'num': 7013 }, 
			        { 'date': "2018-04-9", 'num': 3817 }, 
			        { 'date': "2018-04-10", 'num': 4588 }, 
			        { 'date': "2018-04-11", 'num': 6606 }, 
			        { 'date': "2018-04-12", 'num': 9924 }, 
			        { 'date': "2018-04-13", 'num': 7870 }, 
			        { 'date': "2018-04-14", 'num': 5105 }, 
			        { 'date': "2018-04-15", 'num': 4240 }, 
			        { 'date': "2018-04-16", 'num': 3750 }, 
			        { 'date': "2018-04-17", 'num': 5161 }, 
			        { 'date': "2018-04-18", 'num': 4130 }, 
			        { 'date': "2018-04-19", 'num': 5108 }, 
			        { 'date': "2018-04-20", 'num': 5170 }, 
			        { 'date': "2018-04-21", 'num': 6882 }, 
			        { 'date': "2018-04-22", 'num': 5194 }, 
			        { 'date': "2018-04-23", 'num': 3071 }
    			]
			})

class TicketPresent(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
				{ 'name': '全价票', 'sum': 3216 },
		        { 'name': '套票', 'sum': 15668 },
		        { 'name': '优免票', 'sum': 24383 },
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
			            'sum': 6202,
			            'timePoints': [0 ,0 ,387 ,1616 ,1357 ,516 ,541 ,412 ,587 ,335 ,435 ,16 ,3 ,0 ,0 ,0 ,0] 
			        },
			        { 
			            'name': '外双溪人数',
			            'sum': 2823,
			            'timePoints': [0 ,0 ,123 ,654 ,739 ,125 ,213 ,221 ,365 ,127 ,246 ,7 ,3 ,0 ,0 ,0 ,0] 
			        },
			        { 
			            'name': '金沙人数',
			            'sum': 3382,
			            'timePoints': [0 ,0 ,264 ,962 ,618 ,391 ,328 ,191 ,222 ,208 ,189 ,9 ,0 ,0 ,0 ,0 ,0] 
			        }
				]
			})

class SpotHeat(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 'name': '紫湖', 'id': '001', 'num': 1323, 'x': 0.2, 'y': 0.2 },
                    { 'name': '引浆', 'id': '002', 'num': 419, 'x': 0.4, 'y': 0.3 },
                    { 'name': '中村', 'id': '003', 'num': 523, 'x': 0.5, 'y': 0.6 },
                    { 'name': '双溪', 'id': '004', 'num': 338, 'x': 0.7, 'y': 0.1 },
                    { 'name': '金沙', 'id': '005', 'num': 678, 'x': 0.8, 'y': 0.9 }]
			})

class Cableway(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': {
			        'sumTicket': 5525,
			        'minTicket': 1255,
			        'maxTicket': 1355,
    			}
			})

class VisitorTrend(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 'date': "2018-04-1", 'num': 9593 }, 
		            { 'date': "2018-04-2", 'num': 6278 }, 
		            { 'date': "2018-04-3", 'num': 11974 }, 
		            { 'date': "2018-04-4", 'num': 5987 }, 
		            { 'date': "2018-04-5", 'num': 9795 }, 
		            { 'date': "2018-04-6", 'num': 11926 }, 
		            { 'date': "2018-04-7", 'num': 6082 }, 
		            { 'date': "2018-04-8", 'num': 9013 }, 
		            { 'date': "2018-04-9", 'num': 11817 }, 
		            { 'date': "2018-04-10", 'num': 11588 }, 
		            { 'date': "2018-04-11", 'num': 6606 }, 
		            { 'date': "2018-04-12", 'num': 8924 }, 
		            { 'date': "2018-04-13", 'num': 7870 }, 
		            { 'date': "2018-04-14", 'num': 5105 }, 
		            { 'date': "2018-04-15", 'num': 8240 }, 
		            { 'date': "2018-04-16", 'num': 8750 }, 
		            { 'date': "2018-04-17", 'num': 6161 }, 
		            { 'date': "2018-04-18", 'num': 10130 }, 
		            { 'date': "2018-04-19", 'num': 5108 }, 
		            { 'date': "2018-04-20", 'num': 10170 }, 
		            { 'date': "2018-04-21", 'num': 6882 }, 
		            { 'date': "2018-04-22", 'num': 5194 }, 
		            { 'date': "2018-04-23", 'num': 9071 }, 
		            { 'date': "2018-04-24", 'num': 11158 }, 
		            { 'date': "2018-04-25", 'num': 5908 }, 
		            { 'date': "2018-04-26", 'num': 7067 }, 
		            { 'date': "2018-04-27", 'num': 11006 }, 
		            { 'date': "2018-04-28", 'num': 5459 }, 
		            { 'date': "2018-04-29", 'num': 10964 }, 
		            { 'date': "2018-04-30", 'num': 10021 }
				]
			})

class VisitorForecast(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 'date': "2018-04-1", 'num': 9593 }, 
		            { 'date': "2018-04-2", 'num': 6278 }, 
		            { 'date': "2018-04-3", 'num': 11974 }, 
		            { 'date': "2018-04-4", 'num': 5987 }, 
		            { 'date': "2018-04-5", 'num': 9795 }, 
		            { 'date': "2018-04-6", 'num': 11926 }, 
		            { 'date': "2018-04-7", 'num': 6082 }, 
		            { 'date': "2018-04-8", 'num': 9013 }, 
		            { 'date': "2018-04-9", 'num': 11817 }, 
		            { 'date': "2018-04-10", 'num': 11588 }, 
		            { 'date': "2018-04-11", 'num': 6606 }, 
		            { 'date': "2018-04-12", 'num': 8924 }, 
		            { 'date': "2018-04-13", 'num': 7870 }, 
		            { 'date': "2018-04-14", 'num': 5105 }, 
		            { 'date': "2018-04-15", 'num': 8240 }, 
		            { 'date': "2018-04-16", 'num': 8750 }, 
		            { 'date': "2018-04-17", 'num': 6161 }, 
		            { 'date': "2018-04-18", 'num': 10130 }, 
		            { 'date': "2018-04-19", 'num': 5108 }, 
		            { 'date': "2018-04-20", 'num': 10170 }, 
		            { 'date': "2018-04-21", 'num': 6882 }, 
		            { 'date': "2018-04-22", 'num': 5194 }, 
		            { 'date': "2018-04-23", 'num': 9071 }, 
		            { 'date': "2018-04-24", 'num': 11158 }, 
		            { 'date': "2018-04-25", 'num': 5908 }, 
		            { 'date': "2018-04-26", 'num': 7067 }, 
		            { 'date': "2018-04-27", 'num': 11006 }, 
		            { 'date': "2018-04-28", 'num': 5459 }, 
		            { 'date': "2018-04-29", 'num': 10964 }, 
		            { 'date': "2018-04-30", 'num': 10021 }
				]
			})

class InnerCitySource(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{'name': '赣州市', 'value': 399, 'date': '2018.04.22'},
			        {'name': '吉安市', 'value': 329, 'date': '2018.04.22'},
			        {'name': '上饶市', 'value': 1152, 'date': '2018.04.22'},
			        {'name': '九江市', 'value': 896, 'date': '2018.04.22'},
			        {'name': '抚州市', 'value': 789, 'date': '2018.04.22'},
			        {'name': '宜春市', 'value': 153, 'date': '2018.04.22'},
			        {'name': '南昌市', 'value': 2245, 'date': '2018.04.22'},
			        {'name': '景德镇市', 'value': 1352, 'date': '2018.04.22'},
			        {'name': '萍乡市', 'value': 158, 'date': '2018.04.22'},
			        {'name': '鹰潭市', 'value': 698, 'date': '2018.04.22'},
			        {'name': '新余市', 'value': 830, 'date': '2018.04.22'},]
			})

class OuterCityPercent(tornado.web.RequestHandler):
	def get(self):
		self.finish({
				'code': 1,
				'result': [
					{ 'name': '杭州', 'value': 1233 },
                    { 'name': '上海', 'value': 2534 },
                    { 'name': '广州', 'value': 1643 },
                    { 'name': '东莞', 'value': 3999 },
                    { 'name': '深圳', 'value': 1234 },
                    { 'name': '成都', 'value': 512 },
                    { 'name': '厦门', 'value': 197 },
                    { 'name': '黑龙江', 'value': 7 },
                    { 'name': '昆明', 'value': 345 },
                    { 'name': '大理', 'value': 160 }]
			})

class ParkInfomation(tornado.web.RequestHandler):
	def get(self):
		car1total = random.randint(800, 3000)
		car1used = random.randint(800, 1500)
		car1rest = car1total - car1used
		car2total = random.randint(500, 1000)
		car2used = random.randint(300, 800)
		car2rest = car1total - car1used
		car3total = random.randint(458, 1400)
		car3used = random.randint(300, 1000)
		car3rest = car1total - car1used
		self.finish({
				'code': 1,
				'result': [
					{ 
					'parkName': '金沙停车场',
					'total': car1total,
					'used': car1used,
					'rest': car1rest,
					'detail': [
							{ 'name': '金沙卡口', 'data': [108, 204] },
							{ 'name': '引浆卡口', 'data': [526, 346] },
							{ 'name': '中村卡口', 'data': [123, 415] },
							{ 'name': '双溪卡口', 'data': [157, 198] }
						]
					},
					{ 
					'parkName': '外双溪停车场',
					'total': car2total,
					'used': car2used,
					'rest': car2rest,
					'detail': [
							{ 'name': '金沙卡口', 'data': [108, 204] },
							{ 'name': '引浆卡口', 'data': [526, 346] },
							{ 'name': '中村卡口', 'data': [123, 415] },
							{ 'name': '双溪卡口', 'data': [157, 198] }
						]
					},
					{ 
					'parkName': '枫林停车场',
					'total': car3total,
					'used': car3used,
					'rest': car3rest,
					'detail': [
							{ 'name': '金沙卡口', 'data': [108, 204] },
							{ 'name': '引浆卡口', 'data': [526, 346] },
							{ 'name': '中村卡口', 'data': [123, 415] },
							{ 'name': '双溪卡口', 'data': [157, 198] }
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