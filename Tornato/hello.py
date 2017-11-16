import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import threading
import requests
import time
import json

from boomer import sendMsg2SB

from datetime import datetime

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

userId = 'ba8df3fe0fe84572a76e13616dcba042'
bigTimerInterval = 1800
smallTimerInterval = 300
#获取一天打卡记录
def getSignedList(dayTime):
	r = requests.post('http://124.161.16.163:889/mecp/sys/api/mecp/getSignList.json', {
		'day': dayTime,
		'userId': userId
		})
	return r.json()['results']
#从打卡记录检查是否能够打卡
def canSign(resultList):
	morningSigned = False
	shouldSign = False
	didSign = False
	if len(resultList) == 0:
		return (morningSigned, shouldSign, didSign)
	first = resultList[0]['signTime']
	last = resultList[-1]['signTime']
	firstTime = datetime.strptime(first, '%Y-%m-%d %H:%M')
	lastTime = datetime.strptime(last, '%Y-%m-%d %H:%M')

	now = datetime.now()
	standerTime = datetime(now.year, now.month, now.day, 8, 30, 0)
	standerNoonTime = datetime(now.year, now.month, now.day, 17, 38, 0)

	if lastTime >= standerNoonTime:
		didSign = True
	if firstTime <= standerTime:
		morningSigned = True;
	if morningSigned and didSign == False:
		shouldSign = True
	if now <= standerNoonTime:
		shouldSign = False

	return (morningSigned, shouldSign, didSign)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [(r"/cancle", WordHandler),
					(r"/r", SignResult),
					(r"/", WelComePage)]

		self.isRunning = True
		self.resultText = "刚启动，等会儿！"

		self.timer = threading.Timer(smallTimerInterval, self.checkAndSign)
		self.timer.start()

		self.startTimer = threading.Timer(bigTimerInterval, self.startSign)
		self.startTimer.start()
		# self.checkAndSign();
		day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		results = getSignedList(day)
		canSignObj = canSign(results)
		morningSigned = canSignObj[0]
		shouldSign = canSignObj[1]
		didSign = canSignObj[2]
		if morningSigned:
			self.resultText = "时刻准备着为下午打卡"
		if shouldSign:
			r = requests.post('http://124.161.16.163:889/mecp/sys/api/mecp/Sign.json', {
				'userId': userId
				})
			if r.json()['rCode'] == "0":
				self.resultText = "完成了一天的打卡工作"
		if didSign:
			self.resultText = "已经打卡"

		tornado.web.Application.__init__(self, handlers, debug=True)
#检查并打卡
	def checkAndSign(self):
		print("checkt")
		self.timer = threading.Timer(smallTimerInterval, self.checkAndSign)
		self.timer.start()
		day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		results = getSignedList(day)
		canSignObj = canSign(results)
		morningSigned = canSignObj[0]
		shouldSign = canSignObj[1]
		didSign = canSignObj[2]
		if morningSigned:
			self.resultText = "时刻准备着为下午打卡"
		if shouldSign:
			r = requests.post('http://124.161.16.163:889/mecp/sys/api/mecp/Sign.json', {
				'userId': userId
				})
			if r.json()['rCode'] == "0":
				self.resultText = "完成了一天的打卡工作"
		if didSign:
			self.resultText = "已经打卡"

#开启新一天的打卡系统
	def startSign(self):
		now = datetime.now()
		standerTime = datetime(now.year, now.month, now.day, 9, 0, 0)
		stander0Time = datetime(now.year, now.month, now.day, 1, 0, 0)
		if (now >= stander0Time) and (now <= standerTime):
			self.resultText = "小小姑娘，清早起床。"
		print('time run')
		sendMsg2SB()
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
		self.application.resultText = "今天的自动打卡已经取消了"
		self.write("<h1>取消今天的自动打卡</h1>")
#查询打卡结果
class SignResult(tornado.web.RequestHandler):
	def get(self):
		result = self.application.resultText
		self.write("<h1>%s</h1>" % result)
class WelComePage(tornado.web.RequestHandler):
	"""docstring for  WelComePage"""
	def get(self):
		self.write("<h1>欢迎光临大黄的自动签到</h1><br/><h3>r指令显示签到结果</h3>")
		

if __name__ == '__main__':
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()