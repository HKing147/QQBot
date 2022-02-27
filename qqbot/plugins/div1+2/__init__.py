from nonebot.dependencies import CustomConfig
from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from pprint import pprint
import datetime

s = {
    "div1":
    """美好的一天不如就从ac每日一题开始~！
今天的题目是：
	Div1.&#91; #436. 子串的最大差 &#93;
题目难度：cf *800
题目地址：http://oj.daimayuan.top/problem/436""",
    "div2":
    """美好的一天不如就从ac每日一题开始~！
今天的题目是：
	Div2.&#91; #386. 特殊的正方形 &#93;
题目难度：cf *800
题目地址：http://oj.daimayuan.top/problem/386"""
}

div = on_keyword(['div1', "div2"], priority=2)


@div.handle()
async def div_handle(bot: Bot, event: Event):
    pprint(event.get_plaintext())
    division = event.get_plaintext()
    print("division: ", division)
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
    await setdiv.finish(Message(division + "每日一题设置成功！"))
