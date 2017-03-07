# -*- coding: utf-8 -*-
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__),  os.pardir, '.env')
load_dotenv(dotenv_path)


BOT_NAME = 'instagram'

SPIDER_MODULES = ['instagram.spiders']
NEWSPIDER_MODULE = 'instagram.spiders'

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

# IMAGES_STORE = './images'
# for using local
IMAGES_STORE = os.environ.get("IMAGES_STORE")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY =  os.environ.get("AWS_SECRET_ACCESS_KEY")
