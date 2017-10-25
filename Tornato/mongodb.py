from pymongo import MongoClient

client = MongoClient()

db = client.bookstore
db.books.insert({
	"title": "Programming Collective Intelligence",
	"subtitle": "Building Smart Web 2.0 Applications",
	"image": "/static/images/collective_intelligence.gif",
	"author": "Toby Segaran",
	"date_added": 1310248056,
	"date_released": "August 2009"
	})
db.books.insert({
	"title": "MySql---从删库到跑路",
	"subtitle": "骚年，你渴望力量吗？",
	"image": "这是一张骚气的图片",
	"author": "大黄",
	"date_added": 10100049393,
	"date_released": "未来的2099年"
	})