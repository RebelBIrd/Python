# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import importlib
import os

importlib.reload(sys)

DIR_PATH = '/Users/rebel/Downloads/AV/images/'

class EhentaiImagesPipeline(object):

	def __init__(self):
		self.deal = Deal()

	def process_item(self, item, spider):
		self.save_img(item['image_content'], item['image_name'], item['image_title'])


	def save_img(self, content, file_name, file_title):
		dir_path = self.deal.mkDir(file_title)
		file_path = dir_path + '/' + file_name + '.jpg'
		self.deal.saveImg(content, file_path)
 
class Deal:
    def __init__(self):
        self.path = DIR_PATH
        if not self.path.endswith('/'):
            self.path = self.path + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)
 
    def mkDir(self, path):
        path = path.strip()
        dir_path = self.path + path
        exists = os.path.exists(dir_path)
        if not exists:
            os.makedirs(dir_path)
            return dir_path
        else:
            return dir_path
 
    def saveImg(self, content, path):
        f = open(path, 'wb')
        f.write(content)
        f.close()
 
    def saveBrief(self, content, dir_path, name):
        file_name = dir_path + "/" + name + ".txt"
        f = open(file_name, "w+")
        f.write(content.encode('utf-8'))
 
    def getExtension(self, url):
        extension = url.split('.')[-1]
        return extension
