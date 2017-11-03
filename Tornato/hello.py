import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import threading
import requests
import time
import json

from datetime import datetime

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

userId = 'ba8df3fe0fe84572a76e13616dcba042'
bigTimerInterval = 600
smallTimerInterval = 200
#获取一天打卡记录
def getSignedList(dayTime):
	r = requests.post('http://124.161.16.163:889/mecp/sys/api/mecp/getSignList.json', {
		'day': dayTime,
		'userId': userId
		})
	return r.json()['results']
#从打卡记录检查是否能够打卡
def canSign(resultList):
	if len(resultList) == 0:
		return False
	first = resultList[0]['signTime']
	last = resultList[-1]['signTime']
	firstTime = datetime.strptime(first, '%Y-%m-%d %H:%M')
	lastTime = datetime.strptime(last, '%Y-%m-%d %H:%M')

	now = datetime.now()
	standerTime = datetime(now.year, now.month, now.day, 8, 30, 0)
	standerNoonTime = datetime(now.year, now.month, now.day, 5, 40, 0)
	if now <= standerNoonTime:
		return False
	if lastTime >= standerNoonTime:
		return False
	if firstTime <= standerTime:
		return True

	return False

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [(r"/cancle", WordHandler),
					(r"/r", SignResult)]

		self.isRunning = True
		self.resultText = "今天还没打卡"

		self.timer = threading.Timer(smallTimerInterval, self.checkAndSign)
		self.timer.start()

		self.startTimer = threading.Timer(bigTimerInterval, self.startSign)
		self.startTimer.start()

		tornado.web.Application.__init__(self, handlers, debug=True)
#检查并打卡
	def checkAndSign(self):
		self.timer = threading.Timer(smallTimerInterval, self.checkAndSign)
		self.timer.start()
		day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		results = getSignedList(day)
		if canSign(results):
			r = requests.post('http://124.161.16.163:889/mecp/sys/api/mecp/Sign.json', {
				'userId': userId
				})
			if r.json()['rCode'] == "0":
				self.resultText = "今天打卡成功了"

#开启新一天的打卡系统
	def startSign(self):
		now = datetime.now()
		standerTime = datetime(now.year, now.month, now.day, 9, 0, 0)
		stander0Time = datetime(now.year, now.month, now.day, 1, 0, 0)
		if (now >= stander0Time) and (now <= standerTime):
			self.resultText = "今天还没打卡呢"
		print('time run')
# 打卡定时器如果在运行就啥也不干
		if self.isRunning:
			print('timer alive')
			self.startTimer = threading.Timer(bigTimerInterval, self.startSign)
			self.startTimer.start()
			return
# 当前时间如果在09：00以后，啥也不干，如果是在九点以前，开启打卡定时器。
		if now > standerTime:
			self.startTimer = threading.Timer(bigTimerInterval, self.startSign)
			self.startTimer.start()
			return

		self.timer = threading.Timer(smallTimerInterval, self.checkAndSign)
		self.timer.start()
		self.isRunning = True
		self.startTimer = threading.Timer(bigTimerInterval, self.startSign)
		self.startTimer.start()

#取消一天的自动打卡
class WordHandler(tornado.web.RequestHandler):
	def get(self):
		timer = self.application.timer
		timer.cancel()
		self.application.isRunning = False
		self.write("<h1>取消今天的自动打卡</h1>")
#查询打卡结果
class SignResult(tornado.web.RequestHandler):
	def get(self):
		result = self.application.resultText
		self.write("<h1>%s</h1>" % result)

if __name__ == '__main__':
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()