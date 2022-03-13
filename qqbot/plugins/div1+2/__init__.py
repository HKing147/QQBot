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

# 年轻的ACMER唷～ 你掉的是这道 DIV1 的题目还是这道 DIV2 的题目呢 ～
# Div1.&#91; #454. Minimum Or Spanning Tree &#93;/Div2.&#91; #463. 饿饿 饭饭 &#93;
# 题目难度：cf *1700/cf *1500
# 题目地址：
# http://oj.daimayuan.top/problem/454
# http://oj.daimayuan.top/problem/463"

s = {
    "div1":
    """美好的一天不如就从ac每日一题开始~！
今天的题目是：
	Div1.&#91; #454. Minimum Or Spanning Tree &#93;
题目难度：cf *1700
题目地址：http://oj.daimayuan.top/problem/454""",
    "div2":
    """美好的一天不如就从ac每日一题开始~！
今天的题目是：
	Div2.&#91; #463. 饿饿 饭饭 &#93;
题目难度：cf *1500
题目地址：http://oj.daimayuan.top/problem/463"""
}

def readFile():
    div1=""
    pprint("="*20)
    with open('./data/div1+2/div1.txt','r') as f:
       div1=f.read()
    print(div1)
    pprint("="*20)
    div2=""
    pprint("="*20)
    with open('./data/div1+2/div2.txt','r') as f:
       div2=f.read()
    print(div2)
    pprint("="*20)
    s['div1'] = div1
    s['div2'] = div2
 
def writeFile(content,division):
    path = './data/div1+2/'+division+'.txt'
    pprint(path)
    with open(path,'w+') as f:
        f.write(content)
    return True

div = on_keyword(['div1', "div2"], priority=2)


@div.handle()
async def div_handle(bot: Bot, event: Event):
    readFile()
    pprint(event.get_plaintext())
    division = event.get_plaintext()
    print("division: ", division)
    print(s[division])
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    await div.finish(Message(time + '\n' + s[division]))


# setdiv = on_command("set", permission=SUPERUSER)
setdiv = on_keyword(['set div1', "set div2"], priority=1, permission=SUPERUSER)


@setdiv.handle()
async def setdiv_handle(bot: Bot, event: Event):
    pprint(event.get_plaintext())
    division = event.get_plaintext()[4:8]
    problem = event.get_plaintext()[9:]
    s[division] = problem
    try:
        writeFile(problem,division)
        await setdiv.finish(Message(division + "每日一题设置成功！"))
    except Exception as e:
        pprint(e)
       # await setdiv.finish(Message(division + "每日一题设置失败！"))


# 群发的白名单
# group_id_list=[127792558,523693244]
# group_id_list=[127792558,669633810,728766792,312329114]
group_id_list = [768973940,680787176,830923571,397204493,975489008,984321694,368384017,972152209,230334759,587985749,752832374,
        595700302,838282181,584769166,982015308,793856405,589631009,416352754,747091972,825929430,752778614]

qf = on_command('qf', priority=1, permission=SUPERUSER)
scheduler = require('nonebot_plugin_apscheduler').scheduler
@scheduler.scheduled_job('cron', hour='9',minute='0', id='problem')
@qf.handle()
async def task():
    readFile()
    (bot,) = nonebot.get_bots().values()
    text = "\n快冲！今天的每日一题：\n"
    text = "==========Div1=========\n"+ \
            s['div1'] + \
           "\n==========Div2=========\n" + \
           s['div2']
    url = 'http://acm.mangata.ltd/file/2/learn.jpg'

    for id in group_id_list:
        time.sleep(1)
        try:
            await bot.send_msg(
                message_type="group",
                group_id=int(id),
                message=MessageSegment.image(url) +  text           
            )
        except Exception as e:
            print(e)
