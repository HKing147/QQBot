from nonebot.dependencies import CustomConfig
from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from pprint import pprint
import datetime
import json
import nonebot
import requests
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import require
import random
import time
import  os


# 群发的白名单
# group_id_list=[127792558,523693244]
# group_id_list=[127792558,669633810,728766792,312329114]
# group_id_list = [768973940,680787176,830923571,397204493,975489008,984321694,368384017,972152209,230334759,587985749,752832374,
#         595700302,838282181,584769166,982015308,793856405,589631009,416352754,747091972,825929430]

sjmm = on_command('随机图片', priority=1)
@sjmm.handle()
async def sendImg():
    # url = 'http://acm.mangata.ltd/file/2/learn.jpg'
    # url = 'https://api.btstu.cn/sjbz/api.php?lx=dongman&format=images'
    url = 'http://api.btstu.cn/sjbz/?lx=dongman'
    # url = 'http://api.btstu.cn/sjbz/?lx=meizi'
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    res = requests.get(url=url, headers=headers)
    try:
        await sjmm.finish(Message(MessageSegment.image(url) ))
        # await bot.send_msg(
        #     message_type="group",
        #     group_id=int(id),
        #     message=MessageSegment.image(url) +  text           
        # )
    except Exception as e:
        print(e)
